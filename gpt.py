import openai


def gptTweet(openai_api_key):

    # api key
    openai.api_key = openai_api_key

    # max_tokens
    max_tkns = 14000

    # persona behind Twitter account
    persona = ""

    # what to tweet about
    prompt = ""

    # Use the OpenAI API to generate tweet with given persona
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tkns,
        temperature=0.9,
        top_p=0.5,
        frequency_penalty=1,
        presence_penalty=1
    )
    tweet_content = response['choices'][0]['message']['content']
    return tweet_content()


def gptReply(openai_api_key, read_tweet):

    # api key
    openai.api_key = openai_api_key

    # max_tokens
    max_tkns = 14000

    # persona behind Twitter account
    persona = ""

    # what to tweet about
    prompt = ""

    # Use the OpenAI API to generate tweet with given persona
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": persona},
            {"role": "user", "content": prompt + read_tweet},
        ],
        max_tokens=max_tkns,
        temperature=0.9,
        top_p=0.5,
        frequency_penalty=1,
        presence_penalty=1
    )
    reply_content = response['choices'][0]['message']['content']
    return reply_content()
