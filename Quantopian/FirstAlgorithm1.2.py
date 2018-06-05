
import quantopian.algorithm as algo
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.filters import QTradableStocksUS


def initialize(context):
    
    # Rebalance every day, 15 minutes after market open.
    algo.schedule_function(
        rebalance,
        algo.date_rules.every_day(),
        algo.time_rules.market_open(minutes=15),
    )

    # Record tracking variables at the end of each day.
    algo.schedule_function(
        record_vars,
        algo.date_rules.every_day(),
        algo.time_rules.market_close(),
    )

    # Create our dynamic stock selector.
    algo.attach_pipeline(make_pipeline(), 'pipeline')
    context.assets = []

def make_pipeline():
    
    # Base universe set to the QTradableStocksUS
    base_universe = QTradableStocksUS()
    close_price = USEquityPricing.close.latest

    sentiment_score = SimpleMovingAverage(
        inputs=[stocktwits.bull_minus_bear],
        window_length=3,
    )

    pipe = Pipeline(
        columns={
            'close_price': close_price,
            'sentiment_score':sentiment_score
        },
        screen=base_universe
    )
    return pipe


def before_trading_start(context, data):
    
    context.output = algo.pipeline_output('pipeline')

    # These are the securities that we are interested in trading each day.
    context.security_list = context.output.index
    context.day_count += 1
    log.info(
        context.daily_message.format(
            context.day_count
        )
    )


def rebalance(context, data):
    log.info(context.weekly_message)
    pass


def record_vars(context, data):
    
    pass


def handle_data(context, data):
    
    pass