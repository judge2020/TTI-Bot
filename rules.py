from willie.module import *
ruleslink = ''
@require_privilege(OP)
@commands('rules')
def rules(bot, trigger):
    if not trigger.group(2):
        bot.msg(trigger.nick, 'Please add a name to the command')
    else:
        bot.msg('Chanserv', '%s KICK %s Please read the rules again before re-joining -> %s') % trigger.sender trigger.group(2) ruleslink
