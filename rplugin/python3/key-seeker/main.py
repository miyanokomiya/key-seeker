import neovim
from .lib import seeker


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

    @neovim.command("KeySeekerDig", nargs='1', sync=True)
    def key_seeker_dig(self, args):
        lines = self.nvim.current.buffer[0:]
        cursor_r, cursor_c, hit_key = seeker.dig_key(lines, args[0])
        if hit_key:
            self.set_cursor_pos(cursor_r + 1, cursor_c + 1)
            self.nvim.out_write('Hit: ' + hit_key + '\n')
        else:
            self.nvim.out_write('Not found: ' + args[0] + '\n')

    def get_cursor_pos(self):
        cursor_r, cursor_c = self.nvim.eval('getpos(".")[1:2]')
        return cursor_r, cursor_c

    def set_cursor_pos(self, cursor_r, cursor_c):
        self.nvim.call('cursor', (cursor_r, cursor_c))

    def clip(self, text):
        text = text.replace('"', '\\"')
        self.nvim.command('let @0="{}"'.format(text))
        self.nvim.command('let @"="{}"'.format(text))
        self.nvim.command('let @*="{}"'.format(text))
