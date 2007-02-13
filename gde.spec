Summary:	Tool to manage programming projects
Summary(pl.UTF-8):	Narzędzie do zarządzania projektami programistycznymi
Name:		gde
Version:	0.1.9
Release:	5
License:	GPL
Group:		X11/Development/Tools
Source0:	http://www.student.tue.nl/u/g.zwartjes/ews/download/%{name}-%{version}.tar.gz
# Source0-md5:	d2c3880cf2985196e52c5ac3b7f64a07
Source1:	%{name}.desktop
URL:		http://www.student.tue.nl/u/g.zwartjes/ews/gde.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GTK+ Development Environment (GDE) acts as a framework when you are
programming. It is not an integrated development environment, but more
a tool to manage programming projects. It keeps the user from
switching between terminals and editor windows, with a project
explorer. Making and running a project can be done with function keys,
with commands the user defines.

%description -l pl.UTF-8
GTK+ Development Environment (GDE) służy jako szkielet projektu przy
programowaniu. Nie jest zintegrowanym środowiskiem programistycznym
(IDE), lecz narzędziem do zarządzania projektami programistycznymi.
Przy pomocy przeglądarki projektu uwalnia użytkownika od konieczności
przełączania się pomiędzy terminalami i oknami edytora. Kompilacja i
uruchomienie projektu może być wywołane przez klawisze funkcyjne, przy
pomocy komend podanych przez użytkownika.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/gde.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog NEWS AUTHORS doc/Manual
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
