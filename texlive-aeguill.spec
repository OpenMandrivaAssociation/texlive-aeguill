# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/aeguill
# catalog-date 2009-04-30 00:32:08 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-aeguill
Version:	20090430
Release:	1
Summary:	Add several kinds of guillemets to the ae fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aeguill
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aeguill.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aeguill.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package enables the user to add guillemets from several
source (Polish cmr, Cyrillic cmr, lasy and ec) to the ae fonts.
This was useful when the ae fonts were used to produce PDF
files, since the additional guillemets exist in fonts available
in Adobe Type 1 format.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
