%define name gde
%define version 0.1.9
%define release 1mdk


Version: %{version}
Summary: Tool to manage programming projects
Name: %{name}
Release: %{release}
Copyright: GPL
Group: Development/Other
Source: %{name}-%{version}.tar.bz2
URL: http://www.student.tue.nl/u/g.zwartjes/
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
GTK Development Environment (GDE) acts as a framework when you are programming.
It is not an integrated development environment, but more a tool to manage 
programming projects. It keeps the user from switching between terminals and 
editor windows, with a project explorer. Making and running a project can be 
done with function keys, with commands the user defines.

%prep
rm -rf $RPM_BUILD_ROOT

%setup 

%build

%configure

%make

%install

%makeinstall

(cd $RPM_BUILD_ROOT
mkdir -p ./usr/lib/menu
cat > ./usr/lib/menu/%name <<EOF
?package(%name):\
command="/usr/bin/gde"\
title="Gde"\
longtitle="Programming framework"\
needs="x11"\
section="Applications/Development/Development environments"
EOF
)
 
%post
%update_menus
 
%postun
%clean_menus 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING INSTALL TODO ChangeLog NEWS AUTHORS 
%doc doc/Manual
%_bindir/*
%_menudir/*

%changelog
* Thu Dec 07 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1.9-1mdk
- updated to 0.1.9

* Tue Nov 14 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1.7-1mdk
- new in contribs
- add menu entry
