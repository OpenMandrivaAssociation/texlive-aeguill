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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to add guillemets from several source
(Polish cmr, Cyrillic cmr, lasy and ec) to the ae fonts. This was useful
when the ae fonts were used to produce PDF files, since the additional
guillemets exist in fonts available in Adobe Type 1 format.

