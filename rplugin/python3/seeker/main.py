import neovim
from seeker.lib import seeker


@neovim.plugin
class KeySeeker(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("KeySeekerClip", sync=True)
    def key_seeker_clip(self):
        cursor_r = self.get_cursor_pos()[0]
        lines = self.nvim.current.buffer[:cursor_r]
        key = seeker.seek_key(lines, cursor_r - 1)
        self.clip(key)
        self.nvim.out_write('Clipped: ' + key + '\n')

    def get_cursor_pos(self):
        cursor_r, cursor_c = self.nvim.eval('getpos(".")[1:2]')
        return cursor_r, cursor_c

    def clip(self, text):
        self.nvim.command('let @0="{}"'.format(text))
        self.nvim.command('let @"="{}"'.format(text))
        self.nvim.command('let @*="{}"'.format(text))
