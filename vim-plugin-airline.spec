%define		plugin	airline
Summary:	Vim plugin: Lean & mean status/tabline for vim that's light as air
Name:		vim-plugin-%{plugin}
Version:	0.8
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/vim-airline/vim-airline/archive/v%{version}.tar.gz
# Source0-md5:	d32bc71083c092403bde789a0ae64364
URL:		http://www.vim.org/scripts/script.php?script_id=4661
Requires:	vim-rt >= 4:7.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
A fast and lightweight statusline for Vim that's easily configurable,
extendable, and integrates with powerline font symbols.  It
automatically integrates with a variety of 3rd party plugins and
provides many themes out of the box.

%package doc
Summary:	Documentation for airline Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for airline Vim plugin.

%prep
%setup -qn vim-airline-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/
cp -pr autoload doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_vimdatadir}/autoload/airline.vim
%dir %{_vimdatadir}/autoload/airline
%{_vimdatadir}/autoload/airline/*.vim
%dir %{_vimdatadir}/autoload/airline/extensions
%{_vimdatadir}/autoload/airline/extensions/*.vim
%dir %{_vimdatadir}/autoload/airline/extensions/tabline
%{_vimdatadir}/autoload/airline/extensions/tabline/*.vim
%dir %{_vimdatadir}/autoload/airline/extensions/tabline/formatters
%{_vimdatadir}/autoload/airline/extensions/tabline/formatters/*.vim
%dir %{_vimdatadir}/autoload/airline/extensions/wordcount
%dir %{_vimdatadir}/autoload/airline/extensions/wordcount/formatters
%{_vimdatadir}/autoload/airline/extensions/wordcount/formatters/*.vim
%dir %{_vimdatadir}/autoload/airline/themes
%{_vimdatadir}/autoload/airline/themes/*.vim
%{_vimdatadir}/plugin/airline.vim

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/airline.txt
