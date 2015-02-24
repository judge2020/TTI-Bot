import willie.module
authuser = ''
authpass = ''
@willie.module.commands('auth')
def auth(bot, trigger):
    """
NEVER EVER commmit this password to git
    """
    bot.write(['authserv auth %s %s']) % authuser authpass
