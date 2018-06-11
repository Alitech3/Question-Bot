from disco.bot import Plugin


class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('pong')

    @Plugin.command('test')
    def command_test(self, event):
        event.msg.reply('I pass')

    @Plugin.command('divide', '<a:int> <b:int>', group='math')
    def on_math_dividpi_command(self, event, a, b):
        if a==0:
            return event.msg.reply('can not divide by zero')
        elif b==0:
            return event.msg.reply('can not divide by zero')
        event.msg.reply( '{}'.format(a) + ' goes into ' + '{}'.format(b) + '\n{}'.format(b/a) + ' times' )
        

    @Plugin.command('how many times can', ' <a:int> <b:int>', group='math')
    def on_math_divid_command(self, event, a, b):
        if a==0:
            return event.msg.reply('can not divide by zero')
        elif b==0:
            return event.msg.reply('can not divide by zero')
        event.msg.reply('it goes into ' + '{}'.format(b) + ' {}'.format(b//a) + ' times, with a ' + '{}'.format(b%a) + ' remainder' )    
       
      
      
    @Plugin.command('help')
    def on_help_command(self, event):
         event.msg.reply('Help list version 0.01 \nCOMMANDS\n ping \n test \n im \'content\' \n i wish to file a complaint against \'content\' \n echo \'content\' \n MATH \n math how many times can \'a\' \'b\' \n math add \'a\' \'b\' \n math divide \'a\' \'b\'')


    #'{}'.