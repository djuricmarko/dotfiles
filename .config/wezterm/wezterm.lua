local wezterm = require 'wezterm'
local act = wezterm.action

local config = wezterm.config_builder()

config = {
  default_prog                 = { 'C:\\Program Files\\PowerShell\\7\\pwsh.exe', '-l' },
  initial_rows                 = 60,
  initial_cols                 = 120,
  color_scheme                 = 'Catppuccin Mocha',
  font                         = wezterm.font('JetBrainsMono Nerd Font'),
  font_size                    = 12,
  use_fancy_tab_bar            = false,
  hide_tab_bar_if_only_one_tab = true,
  tab_bar_at_bottom            = true,
  window_close_confirmation    = "NeverPrompt",
  keys                         = {
    { key = "h", mods = "ALT",        action = wezterm.action { ActivatePaneDirection = "Left" } },
    { key = "l", mods = "ALT",        action = wezterm.action { ActivatePaneDirection = "Right" } },
    { key = "k", mods = "ALT",        action = wezterm.action { ActivatePaneDirection = "Up" } },
    { key = "j", mods = "ALT",        action = wezterm.action { ActivatePaneDirection = "Down" } },
    { key = 'w', mods = 'CTRL',       action = wezterm.action.CloseCurrentPane { confirm = false } },
    { key = 's', mods = 'CTRL|SHIFT', action = wezterm.action.SplitHorizontal { domain = 'CurrentPaneDomain' } },
    { key = 'd', mods = 'CTRL|SHIFT', action = wezterm.action.SplitVertical { domain = 'CurrentPaneDomain' } },
    { key = 'u', mods = 'CTRL',       action = act.SpawnTab { DomainName = 'WSL:Ubuntu-24.04', } },
    { key = 'p', mods = 'CTRL',       action = wezterm.action.ActivateCommandPalette },
  }
}

return config

