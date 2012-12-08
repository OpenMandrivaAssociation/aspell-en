%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 7.1-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal english
%define languageeng english
%define languageenglazy American
%define languagecode en
%define lc_ctype en_US

Summary:	English files for aspell
Name:		aspell-%{languagecode}
Version:	7.1.0
Release:	%mkrel 1
Group:		System/Internationalization
Source:		http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%fname-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	SCOWL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides:	spell-%{languagecode}
# old ispell is repalced with aspell
Obsoletes:	ispell-%{languagecode}
Obsoletes:	ispell-english, iamerica, ibritish, ispell-british

BuildRequires:	make
BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Obsoletes:	aspell-en_CA aspell-en_GB
Provides:	aspell-en_CA aspell-en_GB

Autoreqprov:	no

%description
A English dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use %%configure macro
./configure

%make

%install
rm -fr %{buildroot}

%makeinstall_std

chmod 644 README Copyright

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-%{aspell_ver}/*



%changelog
* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 7.1.0-1mdv2012.0
+ Revision: 701857
- New version: 7.1.0

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-11
+ Revision: 662807
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-10mdv2011.0
+ Revision: 603202
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-9mdv2010.1
+ Revision: 518916
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-8mdv2010.0
+ Revision: 413062
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 6.0.0-7mdv2009.1
+ Revision: 350008
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 6.0.0-6mdv2009.0
+ Revision: 220371
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 6.0.0-5mdv2008.1
+ Revision: 182415
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 6.0.0-4mdv2008.1
+ Revision: 148749
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-3mdv2007.0
+ Revision: 123241
- Import aspell-en

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Tue Jan 10 2006 Frederic Crozat <fcrozat@mandriva.com> 6.0.0-2mdk
- rebuild

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 6.0.0-1mdk
- new release

* Wed Aug 11 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 6.0-1mdk
- new release

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.51.1-1mdk
- updated version

