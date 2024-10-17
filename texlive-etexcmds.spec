Name:		texlive-etexcmds
Version:	53171
Release:	2
Summary:	Avoid name clashes with e-TeX commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etexcmds
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etexcmds.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etexcmds.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etexcmds.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
New primitive commands are introduced in e-TeX; sometimes the
names collide with existing macros. This package solves the
name clashes by adding a prefix to e-TeX's commands. For
example, eTeX's \unexpanded is provided as \etex@unexpanded.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/etexcmds
%{_texmfdistdir}/tex/generic/etexcmds
%doc %{_texmfdistdir}/doc/latex/etexcmds

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
