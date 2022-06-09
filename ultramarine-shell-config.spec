
Name:           ultramarine-shell-config
Version:        1.0
Release:        %autorelease
Summary:        Shell configuration for Ultramarine Linux
License:        MIT

Source0:        ultramarine-shell.bash
Source1:        ultramarine-shell.zsh

Source3:        ultramarine-shell.sh
Source4:        starship.toml

Requires:       zsh-autosuggestions
Requires:       zsh-syntax-highlighting
Requires:       exa
Requires:       bat
Requires:       starship

BuildArch:      noarch
%description
This is a very long description of ultramarine-shell-config.

%prep

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
install -pm 644 %{SOURCE0} %{buildroot}/%{_datadir}/%{name}
install -pm 644 %{SOURCE1} %{buildroot}/%{_datadir}/%{name}

install -pm 644 %{SOURCE4} %{buildroot}/%{_datadir}/%{name}


mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/profile.d/


%post

if [ -f %{_sysconfdir}/bashrc ]; then
    # append file to bashrc
    cat %{_datadir}/%{name}/ultramarine-shell.bash >> %{_sysconfdir}/bashrc
fi

if [ -f %{_sysconfdir}/zshrc ]; then
    cat %{_datadir}/%{name}/ultramarine-shell.zsh >> %{_sysconfdir}/zshrc
fi

%files
%{_datadir}/%{name}/
%{_sysconfdir}/profile.d/ultramarine-shell.sh

%changelog
* Wed Jun 08 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.0
- Initial Release
