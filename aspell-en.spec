# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define src_ver %{version}-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal english
%define languageeng english
%define languageenglazy American
%define languagecode en
%define lc_ctype en_US

Summary:	English files for aspell
Name:		aspell-%{languagecode}
Version:	2020.12.07
Release:	2
Group:		System/Internationalization
License:	SCOWL
Url:		http://aspell.sourceforge.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%fname-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-en_CA
Provides:	aspell-en_GB
Provides:	spell-%{languagecode}

Autoreqprov:	no

%description
A English dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use %%configure macro
./configure

%make_build

%install
%make_install

chmod 644 README Copyright

%files
%doc README Copyright
%{_libdir}/aspell-%{aspell_ver}/*
