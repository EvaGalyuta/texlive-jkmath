Name:		jkmath
Version:	0.1
Release:	1
Summary:	Inspired by the physicspackage on CTAN, the package defines some simple macros for mathematical notation which make the code more readable and/or allow flexibility in typesetting material.
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jkmath
License:	The LATEX Project Public License
Source0:	http://ctan.altspu.ru/systems/texlive/tlnet/archive/jkmath.tar.xz
Source1:	http://ctan.altspu.ru/systems/texlive/tlnet/archive/jkmath.doc.tar.xz
BuildArch:	noarch
BuildRequires: texlive-tlpkg
Requires(pre): texlive-tlpkg
Requires(post):texlive-kpathsea	

%description
Inspired by the physicspackage on CTAN, the package defines some simple macros for mathematical notation which make the code more readable and/or allow flexibility in typesetting material.

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/jkmath
%doc %{_texmfdistdir}/doc/latex/jkmath

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
