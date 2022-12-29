Name:		texlive-jlreq
Version:	65119
Release:	1
Summary:	Japanese document class based on requirements for Japanese text layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jlreq
License:	bsd2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jlreq.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a Japanese document class based on
requirements for Japanese text layout. The class file and the
JFM (Japanese font metric) files for LuaTeX-ja / pLaTeX /
upLaTeX are provided.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/jlreq
%{_texmfdistdir}/tex/luatex/jlreq
%{_texmfdistdir}/tex/latex/jlreq
%{_texmfdistdir}/fonts/vf/public/jlreq
%{_texmfdistdir}/fonts/tfm/public/jlreq
%doc %{_texmfdistdir}/doc/latex/jlreq

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
