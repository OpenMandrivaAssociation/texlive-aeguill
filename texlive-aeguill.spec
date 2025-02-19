Name:		texlive-aeguill
Version:	15878
Release:	2
Summary:	Add several kinds of guillemets to the ae fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aeguill
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aeguill.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aeguill.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to add guillemets from several
source (Polish cmr, Cyrillic cmr, lasy and ec) to the ae fonts.
This was useful when the ae fonts were used to produce PDF
files, since the additional guillemets exist in fonts available
in Adobe Type 1 format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/aeguill/aeguill.sty
%doc %{_texmfdistdir}/doc/latex/aeguill/README
%doc %{_texmfdistdir}/doc/latex/aeguill/guil-test1.pdf
%doc %{_texmfdistdir}/doc/latex/aeguill/guil-test1.tex
%doc %{_texmfdistdir}/doc/latex/aeguill/guil-test2.pdf
%doc %{_texmfdistdir}/doc/latex/aeguill/guil-test2.tex
%doc %{_texmfdistdir}/doc/latex/aeguill/license.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
