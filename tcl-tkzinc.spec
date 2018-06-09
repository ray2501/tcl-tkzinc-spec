#
# spec file for package tcl-tkzinc
#

%{!?directory:%define directory /usr}
%define packagename tkzinc

Name:           tcl-tkzinc
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel >= 8.4
BuildRequires:  tk-devel >= 8.4
BuildRequires:  glu-devel
BuildRequires:  glew-devel
Version:        3.3.6
Release:        0
Summary:        A canvas like widget extension to Tcl/Tk
License:        LGPL v2.1
Group:          Development/Languages/Tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            https://bitbucket.org/plecoanet/tkzinc
Source0:        %packagename-%version.tar.gz
Patch0:         PostScript.c.patch

%description
Tkzinc is a canvas like widget extension to Tcl/Tk. It adds
support for ATC displays, provides structured assembly of
items, transformations, clipping, and openGL based rendering
features such as gradients and alpha blending.
    
%prep
%setup -q -n %{packagename}-%{version}
%patch0

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
        --libdir=%{directory}/%{_lib} \
        --with-tcl=%{directory}/%{_lib} \
        --with-tk=%{directory}/%{_lib} \
        --enable-gl=yes
make

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{packagename}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%tcl_archdir

%changelog
