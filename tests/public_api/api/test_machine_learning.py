from opt_out.public_api.api.machine_learning import TextSentimentPrediction


def test_simple():
    prediction = TextSentimentPrediction()
    result = prediction(['You are a lovely person'])
    assert result[0] < .5
