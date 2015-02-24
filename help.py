import willie.module
botname = ''
helplink = ''
@willie.module.commands('help')
def help(bot, trigger):
    bot.msg(trigger.nick, 'The commands for %s are located here -> %s') % botname helplink
