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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple and clear LaTeX template for creating
professional presentations. Featuring dark blue as its primary color,
the theme prioritizes clarity and readability, making it an excellent
choice for researchers, educators, and students.

