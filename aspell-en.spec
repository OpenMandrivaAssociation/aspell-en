%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 6.0-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal english
%define languageeng english
%define languageenglazy American
%define languagecode en
%define lc_ctype en_US

Summary:       English files for aspell
Name:          aspell-%{languagecode}
Version:       6.0.0
Release:       %mkrel 3
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%fname-%{src_ver}.tar.bz2
URL:           http://aspell.sourceforge.net/
License:	   SCOWL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides:	   spell-%{languagecode}
# old ispell is repalced with aspell
Obsoletes:	   ispell-%{languagecode}
Obsoletes:	   ispell-english, iamerica, ibritish, ispell-british

BuildRequires:	make
BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}

# Mandrake Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Obsoletes:	   aspell-en_CA aspell-en_GB
Provides:	   aspell-en_CA aspell-en_GB

Autoreqprov:   no

%description
A English dictionary for use with aspell, a spelling checker.


%prep
%setup -q -n %{fname}-%{src_ver}

%build

# don't use %%configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 README Copyright

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-%{aspell_ver}/*


