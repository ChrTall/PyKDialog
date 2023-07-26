class KDialogCommand(object):

    def __init__(self, command: str, args: list):
        self.option: str = command
        self.args: list = args

    def get_cmd(self) -> str:
        cmd = f'--{self.option}'
        for arg in self.args:
            cmd += f' "{arg}"'
        return cmd
