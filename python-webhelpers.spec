%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: python-webhelpers
Version: 0.6.4
Release: 4%{?dist}
Summary: Helper library for aiding the writing of web templates in Python

Group: Development/Languages
License: BSD
URL: http://pylonshq.com/WebHelpers/
Source0: http://pypi.python.org/packages/source/W/WebHelpers/WebHelpers-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: python-setuptools-devel
BuildRequires: python-nose python-routes python-simplejson
Requires: python-routes >= 1.7, python-simplejson >= 1.4

%description
Web Helpers is a library of helper functions intended to make writing templates
in web applications easier.

One of the sub-sections of Web Helpers contains a full port of the template
helpers that are provided by Ruby on Rails with slight adaptations on occasion
to accommodate for Python.


%prep
%setup -q -n WebHelpers-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%check
PYTHONPATH=$(pwd) nosetests


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 07 2009 Luke Macken <lmacken@redhat.com> - 0.6.4-2
- Remove some non-existent files.

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 0.6.4-1
- Update to 0.6.4
- Run the test suite

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.4-3
- Rebuild for Python 2.6

* Sun May 11 2008 Kyle VanderBeek <kylev@kylev.com> - 0.3.4-2
- Fix rpmlint warnings.
- Add documentation to the package.
- Fix spurious executable bit on CHANGELOG.

* Wed Apr  9 2008 Kyle VanderBeek <kylev@kylev.com> - 0.3.4-1
- Initial version.
