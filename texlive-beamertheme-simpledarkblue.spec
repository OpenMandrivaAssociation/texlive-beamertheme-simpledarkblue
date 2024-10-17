Name:		texlive-beamertheme-simpledarkblue
Version:	60061
Release:	2
Summary:	Template for a simple presentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-simpledarkblue
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpledarkblue.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpledarkblue.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a simple but nice theme for Beamer. Features: simple
structure: with page numbers in footer, no side bar, simple
colors: using only several foreground and background colors.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-simpledarkblue
%doc %{_texmfdistdir}/doc/latex/beamertheme-simpledarkblue

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
