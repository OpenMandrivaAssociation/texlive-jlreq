%global tl_name jlreq
%global tl_revision 79733

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Japanese document class based on requirements for Japanese text layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/jlreq
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Japanese document class based on requirements
for Japanese text layout. The class file and the JFM (Japanese font
metric) files for LuaTeX-ja / pLaTeX / upLaTeX are provided.

