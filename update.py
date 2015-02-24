from willie.module import *
botname = ''
@require_privilege(VOICE) #voice or OP will work
@commands('Update')
def reload_mods(bot, trigger):
    bot.reply('%s has been Updated!') % botname
    bot.setup() #reloads modules
