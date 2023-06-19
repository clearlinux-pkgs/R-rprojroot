#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rprojroot
Version  : 2.0.3
Release  : 63
URL      : https://cran.r-project.org/src/contrib/rprojroot_2.0.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rprojroot_2.0.3.tar.gz
Summary  : Finding Files in Project Subdirectories
Group    : Development/Tools
License  : MIT
BuildRequires : R-mockr
BuildRequires : buildreq-R

%description
a project root. The 'root' of a project is defined as a directory that
    matches a certain criterion, e.g., it contains a certain regular file.

%prep
%setup -q -c -n rprojroot
cd %{_builddir}/rprojroot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649037962

%install
export SOURCE_DATE_EPOCH=1649037962
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rprojroot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rprojroot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rprojroot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rprojroot || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rprojroot/DESCRIPTION
/usr/lib64/R/library/rprojroot/INDEX
/usr/lib64/R/library/rprojroot/LICENSE
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
/usr/lib64/R/library/rprojroot/WORDLIST
/usr/lib64/R/library/rprojroot/doc/index.html
/usr/lib64/R/library/rprojroot/doc/rprojroot.R
/usr/lib64/R/library/rprojroot/doc/rprojroot.Rmd
/usr/lib64/R/library/rprojroot/doc/rprojroot.html
/usr/lib64/R/library/rprojroot/help/AnIndex
/usr/lib64/R/library/rprojroot/help/aliases.rds
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/rprojroot/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/rprojroot/help/paths.rds
/usr/lib64/R/library/rprojroot/help/rprojroot.rdb
/usr/lib64/R/library/rprojroot/help/rprojroot.rdx
/usr/lib64/R/library/rprojroot/html/00Index.html
/usr/lib64/R/library/rprojroot/html/R.css
/usr/lib64/R/library/rprojroot/tests/testthat.R
/usr/lib64/R/library/rprojroot/tests/testthat/_snaps/root.md
/usr/lib64/R/library/rprojroot/tests/testthat/_snaps/testthat.md
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/DESCRIPTION
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/a/b/a
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/a/b/b
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/a/b/c/d
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/a/b/d/e
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/a/remake.yml
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/b
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/c
/usr/lib64/R/library/rprojroot/tests/testthat/hierarchy/hierarchy.Rproj
/usr/lib64/R/library/rprojroot/tests/testthat/package/DESCRIPTION
/usr/lib64/R/library/rprojroot/tests/testthat/package/tests/testthat.R
/usr/lib64/R/library/rprojroot/tests/testthat/package/tests/testthat/test-something.R
/usr/lib64/R/library/rprojroot/tests/testthat/scripts/thisfile-cat.R
/usr/lib64/R/library/rprojroot/tests/testthat/scripts/thisfile.R
/usr/lib64/R/library/rprojroot/tests/testthat/scripts/thisfile.Rmd
/usr/lib64/R/library/rprojroot/tests/testthat/startup.Rs
/usr/lib64/R/library/rprojroot/tests/testthat/test-absolute.R
/usr/lib64/R/library/rprojroot/tests/testthat/test-criterion.R
/usr/lib64/R/library/rprojroot/tests/testthat/test-file.R
/usr/lib64/R/library/rprojroot/tests/testthat/test-path.R
/usr/lib64/R/library/rprojroot/tests/testthat/test-root.R
/usr/lib64/R/library/rprojroot/tests/testthat/test-testthat.R
/usr/lib64/R/library/rprojroot/tests/testthat/vcs/git.zip
/usr/lib64/R/library/rprojroot/tests/testthat/vcs/svn.zip
