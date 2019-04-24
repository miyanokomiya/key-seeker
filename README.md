# key-seeker.nvim
Simple key seeker (e.g. for i18n resource files)

## Requirements
python3 & [Pynvim](https://github.com/neovim/pynvim)


## Installation
.dein_lazy.toml
```toml
[[plugins]]
repo = 'miyanokomiya/key-seeker.nvim'
on_cmd    = ['KeySeekerClip', 'KeySeekerDig']
# optional
hook_add = '''
nnoremap <silent> <Space>s :KeySeekerClip<CR>
'''
```

## Usage
Execute the command on a line to clip the joined key.
```
:KeySeekerClip
```

json
```json
{
  "a": {
    "b": {
      "c": ":KeySeekerClip -> Clip 'a.b.c'"
    }
  }
}
```

yaml
```yaml
a:
  b:
    c: ":KeySeekerClip -> Clip 'a.b.c'"
```

Execute the command to go to the line.
```
:KeySeekerDig <key>
```

json
```json
{
  "a": {
    "b": {
      "c": ":KeySeekerDig a.b.c -> go to this line"
    }
  }
}
```

## Limitation
### Multi Keys on a line
NG
```json
{
  "a": "a", "b": ":KeySeekerClip -> Clip 'a'"
}
```

### Keys include ":"
NG
```json
{
  "a:b": {
    "c": ":KeySeekerClip -> Clip 'a.c'",
  }
}
```
