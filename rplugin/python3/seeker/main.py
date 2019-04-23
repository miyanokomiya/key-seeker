import neovim
from lib import seeker


@neovim.plugin
class KeySeeker(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("KeySeekerClip", sync=True)
    def key_seeker_clip(self):
        cursor_r = self.get_cursor_pos(self.nvim)[0]
        lines = self.nvim.current.buffer[:cursor_r]
        key = seeker.seek_key(lines, cursor_r - 1)
        self.clip(self.nvim, key)
        self.nvim.out_write('Clipped: ' + key + '\n')

    def get_cursor_pos(self):
        cursor_r, cursor_c = self.nvim.eval('getpos(".")[1:2]')
        return cursor_r, cursor_c

    def clip(self, text):
        self.command('let @0="{}"'.format(text))
        self.command('let @"="{}"'.format(text))
        self.command('let @*="{}"'.format(text))
