#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pROC
Version  : 1.15.0
Release  : 1
URL      : https://cran.r-project.org/src/contrib/pROC_1.15.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pROC_1.15.0.tar.gz
Summary  : Display and Analyze ROC Curves
Group    : Development/Tools
License  : GPL-3.0
Requires: R-pROC-lib = %{version}-%{release}
Requires: R-ggplot2
Requires: R-logcondens
Requires: R-plyr
BuildRequires : R-ggplot2
BuildRequires : R-logcondens
BuildRequires : R-plyr
BuildRequires : buildreq-R

%description
[![Build Status](https://travis-ci.org/xrobin/pROC.svg?branch=master)](https://travis-ci.org/xrobin/pROC)
[![AppVeyor build status](https://ci.appveyor.com/api/projects/status/github/xrobin/pROC?branch=master&svg=true)](https://ci.appveyor.com/project/xrobin/pROC)
[![Codecov coverage](https://codecov.io/github/xrobin/pROC/branch/master/graphs/badge.svg)](https://codecov.io/github/xrobin/pROC)
[![CRAN Version](http://www.r-pkg.org/badges/version/pROC)](https://cran.r-project.org/package=pROC)
[![Downloads](http://cranlogs.r-pkg.org/badges/pROC)](https://cran.r-project.org/package=pROC)

%package lib
Summary: lib components for the R-pROC package.
Group: Libraries

%description lib
lib components for the R-pROC package.


%prep
%setup -q -c -n pROC

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560139275

%install
export SOURCE_DATE_EPOCH=1560139275
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pROC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pROC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pROC
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pROC || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pROC/CITATION
/usr/lib64/R/library/pROC/DESCRIPTION
/usr/lib64/R/library/pROC/INDEX
/usr/lib64/R/library/pROC/Meta/Rd.rds
/usr/lib64/R/library/pROC/Meta/data.rds
/usr/lib64/R/library/pROC/Meta/features.rds
/usr/lib64/R/library/pROC/Meta/hsearch.rds
/usr/lib64/R/library/pROC/Meta/links.rds
/usr/lib64/R/library/pROC/Meta/nsInfo.rds
/usr/lib64/R/library/pROC/Meta/package.rds
/usr/lib64/R/library/pROC/NAMESPACE
/usr/lib64/R/library/pROC/NEWS
/usr/lib64/R/library/pROC/R/pROC
/usr/lib64/R/library/pROC/R/pROC.rdb
/usr/lib64/R/library/pROC/R/pROC.rdx
/usr/lib64/R/library/pROC/data/aSAH.RData
/usr/lib64/R/library/pROC/extra/algorithms.speed.test.R
/usr/lib64/R/library/pROC/extra/bench/fig-unnamed-chunk-13-1.png
/usr/lib64/R/library/pROC/extra/bench/fig-unnamed-chunk-5-1.png
/usr/lib64/R/library/pROC/extra/bench/fig-unnamed-chunk-9-1.png
/usr/lib64/R/library/pROC/extra/benchmark.Rmd
/usr/lib64/R/library/pROC/extra/benchmark.md
/usr/lib64/R/library/pROC/extra/sos_clashes.R
/usr/lib64/R/library/pROC/help/AnIndex
/usr/lib64/R/library/pROC/help/aliases.rds
/usr/lib64/R/library/pROC/help/pROC.rdb
/usr/lib64/R/library/pROC/help/pROC.rdx
/usr/lib64/R/library/pROC/help/paths.rds
/usr/lib64/R/library/pROC/html/00Index.html
/usr/lib64/R/library/pROC/html/R.css
/usr/lib64/R/library/pROC/tests/figs/deps.txt
/usr/lib64/R/library/pROC/tests/figs/ggroc/ggroc-list-extra-aes-screenshot.svg
/usr/lib64/R/library/pROC/tests/figs/ggroc/ggroc-list-group-facet-screenshot.svg
/usr/lib64/R/library/pROC/tests/figs/ggroc/ggroc-list-multi-aes.svg
/usr/lib64/R/library/pROC/tests/figs/ggroc/ggroc-list-screenshot.svg
/usr/lib64/R/library/pROC/tests/figs/ggroc/ggroc-screenshot.svg
/usr/lib64/R/library/pROC/tests/figs/plot/advanced-screenshot-1.svg
/usr/lib64/R/library/pROC/tests/figs/plot/advanced-screenshot-2.svg
/usr/lib64/R/library/pROC/tests/figs/plot/advanced-screenshot-3.svg
/usr/lib64/R/library/pROC/tests/figs/plot/advanced-screenshot-4.svg
/usr/lib64/R/library/pROC/tests/figs/plot/advanced-screenshot-5.svg
/usr/lib64/R/library/pROC/tests/figs/plot/advanced-screenshot-6.svg
/usr/lib64/R/library/pROC/tests/figs/plot/basic-ndka.svg
/usr/lib64/R/library/pROC/tests/figs/plot/basic-s100b.svg
/usr/lib64/R/library/pROC/tests/figs/plot/basic-wfns.svg
/usr/lib64/R/library/pROC/tests/figs/plot/legacy-axes.svg
/usr/lib64/R/library/pROC/tests/figs/plot/plot-formula.svg
/usr/lib64/R/library/pROC/tests/testthat.R
/usr/lib64/R/library/pROC/tests/testthat/helper-coords-expected.R
/usr/lib64/R/library/pROC/tests/testthat/helper-deLongPlacementsCpp-expected.R
/usr/lib64/R/library/pROC/tests/testthat/helper-expect_equal_roc.R
/usr/lib64/R/library/pROC/tests/testthat/helper-roc-expected.R
/usr/lib64/R/library/pROC/tests/testthat/helper-rocs.R
/usr/lib64/R/library/pROC/tests/testthat/print_output/multiclass
/usr/lib64/R/library/pROC/tests/testthat/print_output/multiclass_levels
/usr/lib64/R/library/pROC/tests/testthat/print_output/multiclass_partial
/usr/lib64/R/library/pROC/tests/testthat/print_output/multiclass_partial_correct
/usr/lib64/R/library/pROC/tests/testthat/print_output/multiclass_partial_se
/usr/lib64/R/library/pROC/tests/testthat/print_output/multiclass_percent
/usr/lib64/R/library/pROC/tests/testthat/print_output/mv_multiclass
/usr/lib64/R/library/pROC/tests/testthat/print_output/mv_multiclass.ndka.formula
/usr/lib64/R/library/pROC/tests/testthat/print_output/mv_multiclass_levels
/usr/lib64/R/library/pROC/tests/testthat/print_output/mv_multiclass_partial
/usr/lib64/R/library/pROC/tests/testthat/print_output/mv_multiclass_partial_correct
/usr/lib64/R/library/pROC/tests/testthat/print_output/mv_multiclass_partial_se
/usr/lib64/R/library/pROC/tests/testthat/print_output/mv_multiclass_percent
/usr/lib64/R/library/pROC/tests/testthat/print_output/ndka_formula
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.ndka
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.ndka.formula
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.ndka.formula.ci
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.ndka.formula.no_auc
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.ndka.partial1
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.ndka.percent
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.ndka.percent.partial1
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.s100b
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.s100b.partial1
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.s100b.partial2
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.s100b.percent
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.s100b.percent.partial1
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.wfns
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.wfns.partial1
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.wfns.percent
/usr/lib64/R/library/pROC/tests/testthat/print_output/r.wfns.percent.partial1
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.ndka
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.s100b.binormal
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.s100b.density
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.s100b.fitdistr
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.s100b.formula
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.s100b.logcondens
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.s100b.logcondens.smooth
/usr/lib64/R/library/pROC/tests/testthat/print_output/smooth.wfns
/usr/lib64/R/library/pROC/tests/testthat/test-Ops.R
/usr/lib64/R/library/pROC/tests/testthat/test-are-paired.R
/usr/lib64/R/library/pROC/tests/testthat/test-auc.R
/usr/lib64/R/library/pROC/tests/testthat/test-ci.auc.R
/usr/lib64/R/library/pROC/tests/testthat/test-ci.coords.R
/usr/lib64/R/library/pROC/tests/testthat/test-coords.R
/usr/lib64/R/library/pROC/tests/testthat/test-cov.R
/usr/lib64/R/library/pROC/tests/testthat/test-deLongPlacementsCpp.R
/usr/lib64/R/library/pROC/tests/testthat/test-ggroc.R
/usr/lib64/R/library/pROC/tests/testthat/test-large.R
/usr/lib64/R/library/pROC/tests/testthat/test-multiclass.R
/usr/lib64/R/library/pROC/tests/testthat/test-numeric-Inf.R
/usr/lib64/R/library/pROC/tests/testthat/test-numeric-accuracy.R
/usr/lib64/R/library/pROC/tests/testthat/test-onload.R
/usr/lib64/R/library/pROC/tests/testthat/test-plot.R
/usr/lib64/R/library/pROC/tests/testthat/test-power.roc.test.R
/usr/lib64/R/library/pROC/tests/testthat/test-print.R
/usr/lib64/R/library/pROC/tests/testthat/test-roc.R
/usr/lib64/R/library/pROC/tests/testthat/test-roc.test.R
/usr/lib64/R/library/pROC/tests/testthat/test-roc.utils.R
/usr/lib64/R/library/pROC/tests/testthat/test-roc.utils.percent.R
/usr/lib64/R/library/pROC/tests/testthat/test-var.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pROC/libs/pROC.so
/usr/lib64/R/library/pROC/libs/pROC.so.avx2
