from quantopian.algorithm import (
    attach_pipeline,
    pipeline_output,
    order_optimal_portfolio,
)


import quantopian.optimize as opt


from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.psychsignal import stocktwits
from quantopian.pipeline.factors import SimpleMovingAverage


from quantopian.pipeline.filters import QTradableStocksUS
from quantopian.pipeline.experimental import risk_loading_pipeline

from quantopian.pipeline.data.builtin import USEquityPricing


def initialize(context):
    # Restricciones &&
    context.max_lever = 1.2
    context.max_posTam = 0.025
    # Volumen de Negocios
    context.max_Volum = 0.85

    # adjunta la informacion de pipelines
    attach_pipeline(make_pipeline(),'data_pipe')
    attach_pipeline(risk_loading_pipeline(),'risk_pipe')

    # llama la funcion rebalance cada dia, 15 minutos despues que el mercado abre
    schedule_function(
        rebalance,
        date_rules.week_start(),
        time_rules.market_open(minutes=15),
    )


def before_trading_start(context, data):
    # Obtiene la salida del pipeline y la guarda en context
    context.output = pipeline_output('data_pipe')
	context.risk_factor_betas = pipeline_output('risk_pipe')


# Pipeline definition
def make_pipeline():

    sentiment_score = SimpleMovingAverage(
        inputs=[stocktwits.bull_minus_bear],
        window_length=4,
        mask=QTradableStocksUS()
    )
    close_price = USEquityPricing.close.latest
	return Pipeline(
        columns={
           	'close_price':close_price,
            'sentiment_score': sentiment_score,
        },
        screen=sentiment_score.notnull()
    )


def rebalance(context, data):
    
    objective = opt.MaximizeAlpha(
      context.output.sentiment_score
    )

    # Create position size constraint
    constrain_posTam = opt.PositionConcentration.with_equal_bounds(-1.5*context.max_posTam,context.max_posTam)

    # Ensure long and short books
    # are roughly the same size
    dollar_neutral = opt.DollarNeutral()

    # Constrain target portfolio's lever
    max_lever = opt.MaxGrossExposure(context.max_lever)

    # Constrain portfolio Volum
    max_Volum = opt.MaxTurnover(context.max_Volum)

    
    factor_risk_constraints = opt.experimental.RiskModelExposure(
        context.risk_factor_betas,
        version=opt.Newest
    )

    # Rebalance portfolio using objective
    # and list of constraints
    order_optimal_portfolio(
        objective=objective,
        constraints=[
            max_lever,
            dollar_neutral,
            constrain_posTam,
            max_Volum,
            factor_risk_constraints,
        ]
    )
