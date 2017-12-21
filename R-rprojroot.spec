#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rprojroot
Version  : 1.3.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/rprojroot_1.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rprojroot_1.3-1.tar.gz
Summary  : Finding Files in Project Subdirectories
Group    : Development/Tools
License  : GPL-3.0
Requires: R-backports
Requires: R-withr
BuildRequires : R-backports
BuildRequires : R-withr
BuildRequires : clr-R-helpers

%description
project root. The 'root' of a project is defined as a directory
    that matches a certain criterion, e.g., it contains a certain
    regular file.

%prep
%setup -q -c -n rprojroot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513873878

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1513873878
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rprojroot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rprojroot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rprojroot|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rprojroot/DESCRIPTION
/usr/lib64/R/library/rprojroot/INDEX
/usr/lib64/R/library/rprojroot/Meta/Rd.rds
/usr/lib64/R/library/rprojroot/Meta/features.rds
/usr/lib64/R/library/rprojroot/Meta/hsearch.rds
/usr/lib64/R/library/rprojroot/Meta/links.rds
/usr/lib64/R/library/rprojroot/Meta/nsInfo.rds
/usr/lib64/R/library/rprojroot/Meta/package.rds
/usr/lib64/R/library/rprojroot/Meta/vignette.rds
/usr/lib64/R/library/rprojroot/NAMESPACE
/usr/lib64/R/library/rprojroot/NEWS.md
/usr/lib64/R/library/rprojroot/R/rprojroot
/usr/lib64/R/library/rprojroot/R/rprojroot.rdb
/usr/lib64/R/library/rprojroot/R/rprojroot.rdx
/usr/lib64/R/library/rprojroot/doc/index.html
/usr/lib64/R/library/rprojroot/doc/rprojroot.R
/usr/lib64/R/library/rprojroot/doc/rprojroot.Rmd
/usr/lib64/R/library/rprojroot/doc/rprojroot.html
/usr/lib64/R/library/rprojroot/help/AnIndex
/usr/lib64/R/library/rprojroot/help/aliases.rds
/usr/lib64/R/library/rprojroot/help/paths.rds
/usr/lib64/R/library/rprojroot/help/rprojroot.rdb
/usr/lib64/R/library/rprojroot/help/rprojroot.rdx
/usr/lib64/R/library/rprojroot/html/00Index.html
/usr/lib64/R/library/rprojroot/html/R.css
