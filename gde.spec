Summary:	Tool to manage programming projects
Summary(pl):	Narzêdzie do zarz±dzania projektami programistycznymi
Name:		gde
Version:	0.1.9
Release:	2
License:	GPL
Group:		X11/Development/Tools
Source0:	http://www.student.tue.nl/u/g.zwartjes/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.student.tue.nl/u/g.zwartjes/gde.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
GTK Development Environment (GDE) acts as a framework when you are
programming. It is not an integrated development environment, but more
a tool to manage programming projects. It keeps the user from
switching between terminals and editor windows, with a project
explorer. Making and running a project can be done with function keys,
with commands the user defines.

%description -l pl
GTK Development Environment (GDE) zapewnia ci podczas programowania
odpowiedni szkielet projektu. Nie jest zintegrowanym ¶rodowiskiem
programistycznym (IDE), lecz narzêdziem do zarz±dzania projektami
programistycznymi. Przy pomocy przegl±darki projektu uwalnia
u¿ytkownika od konieczno¶ci prze³±czania siê pomiêdzy terminalami i
oknami edytora. Kompilacja i uruchomienie projektu mo¿e byæ wywo³ane
przez klawisze funkcyjne, przy pomocy komend podanych przez
u¿ytkownika.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development/gde.desktop

gzip -9nf README TODO ChangeLog NEWS AUTHORS doc/Manual

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Development/*
