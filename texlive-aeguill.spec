%global tl_name aeguill
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Add several kinds of guillemets to the ae fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aeguill
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aeguill.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aeguill.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to add guillemets from several source
(Polish cmr, Cyrillic cmr, lasy and ec) to the ae fonts. This was useful
when the ae fonts were used to produce PDF files, since the additional
guillemets exist in fonts available in Adobe Type 1 format.

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
%dir %{_datadir}/texmf-dist/doc/latex/aeguill
%dir %{_datadir}/texmf-dist/tex/latex/aeguill
%doc %{_datadir}/texmf-dist/doc/latex/aeguill/README
%doc %{_datadir}/texmf-dist/doc/latex/aeguill/guil-test1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aeguill/guil-test1.tex
%doc %{_datadir}/texmf-dist/doc/latex/aeguill/guil-test2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/aeguill/guil-test2.tex
%doc %{_datadir}/texmf-dist/doc/latex/aeguill/license.txt
%{_datadir}/texmf-dist/tex/latex/aeguill/aeguill.sty
