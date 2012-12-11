%define major   3.2

Name:           yum
Version:        3.2.29
Release:        %mkrel 1
Summary:        RPM installer/updater
License:        GPLv3+
Group:          System/Configuration/Packaging
Source:         http://linux.duke.edu/projects/yum/download/%{major}/%{name}-%{version}.tar.gz
URL:            http://www.linux.duke.edu/projects/yum
Requires:       python-rpm
Requires:       python-libxml2
Requires:       python-urlgrabber
Requires:       python-celementtree
Requires:       python-gpgme
Requires:       python-iniparse
Requires:       yum-metadata-parser
BuildRequires:  python-devel
BuildRequires:	gettext
BuildRequires:  intltool
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded
automatically prompting the user as necessary.

%prep
%setup -q

%build
%{make}

%install
rm -rf %{buildroot}
%{makeinstall_std}
# correct scripts
perl -pi -e 's|%{_libdir}/yum|%{_datadir}/yum|' %{buildroot}%{_bindir}/*
# remove init stuff
rm -f %{buildroot}%{_sysconfdir}/cron.*/yum.cron
rm -f %{buildroot}%{_sysconfdir}/init.d/%{name}
rm -f %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
rm -f %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
rm -Rf  %{buildroot}/%py_puresitedir/urlgrabber/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc README AUTHORS COPYING TODO INSTALL
%config(noreplace) %{_sysconfdir}/yum/
%py_puresitedir/*
%{_datadir}/yum-cli/
%{_bindir}/*
%{_sbindir}/*
/var/cache/yum
%{_sysconfdir}/bash_completion.d/yum.bash
%{_mandir}/man*/*
%{_sysconfdir}/rc.d/init.d/yum-updatesd
%{_sysconfdir}/cron.daily/0yum.cron
%{_sysconfdir}/rc.d/init.d/yum-cron
%{_sysconfdir}/sysconfig/yum-cron
%attr(0644,root,root) %{_sysconfdir}/dbus-1/system.d/yum-updatesd.conf


%changelog
* Tue Mar 08 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.2.29-1mdv2011.0
+ Revision: 642892
- new version
- update file list

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 3.2.28-2mdv2011.0
+ Revision: 590092
- rebuild for python 2.7

* Sun Oct 17 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.28-1mdv2011.0
+ Revision: 586375
- update to 3.2.28

* Wed Apr 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.2.27-1mdv2010.1
+ Revision: 537458
- update to new version

* Tue Nov 10 2009 Michael Scherer <misc@mandriva.org> 3.2.25-1mdv2010.1
+ Revision: 463855
- update to new version 3.2.25

* Tue Sep 29 2009 Michael Scherer <misc@mandriva.org> 3.2.24-1mdv2010.0
+ Revision: 450815
- new version
- fix build on x86_64

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 3.2.21-2mdv2010.0
+ Revision: 446312
- rebuild

* Thu Jan 15 2009 JÃ©rÃ´me Soyer <saispo@mandriva.org> 3.2.21-1mdv2009.1
+ Revision: 329835
- New upstream release

* Fri Jan 09 2009 JÃ©rÃ´me Soyer <saispo@mandriva.org> 3.2.20-1mdv2009.1
+ Revision: 327616
- New upstream version

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 3.2.19-3mdv2009.1
+ Revision: 318410
- rebuild for new python

* Fri Sep 12 2008 Alexander Kurtakov <akurtakov@mandriva.org> 3.2.19-2mdv2009.0
+ Revision: 284123
- Requires python-iniparse

* Fri Sep 12 2008 Alexander Kurtakov <akurtakov@mandriva.org> 3.2.19-1mdv2009.0
+ Revision: 284119
- new version 3.2.19

* Tue Jul 15 2008 Alexander Kurtakov <akurtakov@mandriva.org> 3.2.17-1mdv2009.0
+ Revision: 235742
- new version 3.2.17

* Mon Jun 30 2008 Alexander Kurtakov <akurtakov@mandriva.org> 3.2.16-1mdv2009.0
+ Revision: 230219
- add missing BRs
- new version 3.2.16

* Mon Jun 30 2008 Alexander Kurtakov <akurtakov@mandriva.org> 3.2.10-2mdv2009.0
+ Revision: 230150
- add missing requires

* Sun Mar 02 2008 Michael Scherer <misc@mandriva.org> 3.2.10-1mdv2008.1
+ Revision: 177636
- update to new version 3.2.10

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.2-3mdv2008.0
+ Revision: 90398
- rebuild

* Sat Aug 11 2007 David Walluck <walluck@mandriva.org> 3.2.2-2mdv2008.0
+ Revision: 62014
- make yum-updatesd.conf non-executable

* Sat Aug 11 2007 David Walluck <walluck@mandriva.org> 3.2.2-1mdv2008.0
+ Revision: 61688
- 3.2.2


* Tue Dec 05 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 3.0.1-1mdv2007.0
+ Revision: 90600
- Sync sources
- New release 3.0.1
- import yum-2.6.1-1mdk

* Sat May 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.6.1-1mdk
- New release 2.6.1

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.0-1mdk
- New release 2.6.0

* Mon Dec 05 2005 Michael Scherer <misc@mandriva.org> 2.4.0-2mdk
- requires python-celementtree ( fix bug #19895 )

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 2.4.0-1mdk
- New release 2.4.0

* Sat Sep 10 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.2-3mdk
- fix requires

* Fri Sep 02 2005 Michael Scherer <misc@mandriva.org> 2.2.2-2mdk
- remove bundled urlgrabber
- use python macro

* Fri Jul 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.2.2-1mdk
- New release 2.2.2

* Sat Jun 04 2005 Götz Waschk <waschk@mandriva.org> 2.2.1-3mdk
- obsolete python-urlgrabber

* Sun Apr 10 2005 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.1-2mdk 
- fix URL (fix bug #14822)
- spec cleanup

* Sat Mar 19 2005 Michael Scherer <misc@mandrake.org> 2.2.1-1mdk
- new version

* Thu May 27 2004 Michael Scherer <misc@mandrake.org> 2.0.7-1mdk
- New release 2.0.7
- add a notice about the recompression

* Wed May 26 2004 Michael Scherer <misc@mandrake.org> 2.0.6-2mdk 
- add correct Requires
- remove warning in description

* Fri Apr 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.0.6-1mdk
- new version
- rpmbuildupdate aware

