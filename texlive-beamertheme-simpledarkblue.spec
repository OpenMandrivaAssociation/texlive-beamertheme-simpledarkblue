%global tl_name beamertheme-simpledarkblue
%global tl_revision 73454

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Template for a simple presentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-simpledarkblue
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpledarkblue.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-simpledarkblue.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple and clear LaTeX template for creating
professional presentations. Featuring dark blue as its primary color,
the theme prioritizes clarity and readability, making it an excellent
choice for researchers, educators, and students.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-simpledarkblue
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-simpledarkblue
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpledarkblue/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpledarkblue/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpledarkblue/beamertheme-simpledarkblue-sample.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpledarkblue/beamertheme-simpledarkblue-sample.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-simpledarkblue/reference.bib
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpledarkblue/beamercolorthemeSimpleDarkBlue.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpledarkblue/beamerfontthemeSimpleDarkBlue.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpledarkblue/beamerinnerthemeSimpleDarkBlue.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-simpledarkblue/beamerthemeSimpleDarkBlue.sty
