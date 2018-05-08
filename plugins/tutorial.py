from disco.bot import Plugin


class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('pong')

    @Plugin.command('test')
    def command_test(self, event):
        event.msg.reply('I pass')

    @Plugin.command('add', '<a:int> <b:int>', group='math')
    def on_math_add_command(self, event, a, b):
        # Commands can be grouped together for a cleaner user-facing interface.
        event.msg.reply('It is ' + '{}'.format(a + b))

    @Plugin.command('i wish to file a complaint against', ' <content:str...>')
    @Plugin.command('im', ' <content:str...>')
    def on_im_command(self, event, content):
        event.msg.reply(content + '... you\'re fired.')

    @Plugin.command('echo' '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)

    #'{}'.