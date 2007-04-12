%define name	yum
%define major	3.0
%define version 3.0.1
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	RPM installer/updater
License:	GPL
Group:		System/Configuration/Packaging
# for some strange ( read RH use a incompatible gzip release ) reason, you may need to recompress this file.
Source:		http://linux.duke.edu/projects/yum/download/%{major}/%{name}-%{version}.tar.bz2
URL:		http://www.linux.duke.edu/projects/yum
Requires:       python-rpm
Requires:       python-libxml2
Requires:	python-urlgrabber
Requires:	python-celementtree
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded 
automatically prompting the user as necessary.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std
# correct scripts
perl -pi -e 's|%{_libdir}/yum|%{_datadir}/yum|' %{buildroot}%{_bindir}/*
# remove init stuff
rm -f %{buildroot}%{_sysconfdir}/cron.*/yum.cron
rm -f %{buildroot}%{_sysconfdir}/init.d/%{name}
rm -f %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
rm -f %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
rm -Rf  %{buildroot}/%py_sitedir/urlgrabber/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc README AUTHORS COPYING TODO INSTALL
%config(noreplace) %{_sysconfdir}/yum.conf
%config(noreplace) %{_sysconfdir}/yum/
%py_sitedir/*
%{_datadir}/yum-cli/
%{_bindir}/*
%{_sbindir}/*
/var/cache/yum
%{_mandir}/man*/*
%{_sysconfdir}/rc.d/init.d/yum-updatesd
%{_sysconfdir}/dbus-1/system.d/yum-updatesd.conf


