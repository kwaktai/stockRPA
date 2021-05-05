from slacker import Slacker

slack = Slacker('xoxb-1731659647985-1712312144294-jkXtirCOy5vLmn3CgmuZL1oZ')

strbuf = "test111"
slack.chat.post_message('#stock', strbuf)
