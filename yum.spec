%define major   3.2

Name:			yum
Version:		3.2.29
Release:		4
Summary:		RPM installer/updater
License:		GPLv3+
Group:			System/Configuration/Packaging
Source0:		http://linux.duke.edu/projects/yum/download/%{major}/%{name}-%{version}.tar.gz
URL:			https://www.linux.duke.edu/projects/yum
Requires:		python-rpm
Requires:		python-libxml2
Requires:		python-urlgrabber
Requires:		python2-celementtree
Requires:		python-gpgme
Requires:		python-iniparse
Requires:		yum-metadata-parser
BuildRequires:	pkgconfig(python2)
BuildRequires:	gettext
BuildRequires:	intltool
BuildArch:		noarch

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded
automatically prompting the user as necessary.

%prep
%setup -q

%build
export PYTHON=%{__python2}
%make PYTHON=%{__python2}

%install
%{makeinstall_std} PYTHON=%{__python2}

# correct scripts
perl -pi -e 's|%{_libdir}/yum|%{_datadir}/yum|' %{buildroot}%{_bindir}/*
# remove init stuff
rm -f %{buildroot}%{_sysconfdir}/cron.*/yum.cron
rm -f %{buildroot}%{_sysconfdir}/init.d/%{name}
rm -f %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
rm -f %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
rm -Rf  %{buildroot}/%py2_puresitedir/urlgrabber/

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS COPYING TODO INSTALL
%config(noreplace) %{_sysconfdir}/yum/
%py2_puresitedir/*
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


