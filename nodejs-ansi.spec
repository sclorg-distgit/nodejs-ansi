%{?scl:%scl_package nodejs-ansi}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:		%{?scl_prefix}nodejs-ansi
Version:	0.3.0
Release:	2%{?dist}
Summary:	ANSI escape codes for Node.js
License:	MIT
URL:		https://github.com/TooTallNate/ansi.js

# the source contains a nonfree image file, which is removed by the Source1 script
#Source0:	ansi-%{version}-stripped.tgz
#Source1:	nodejs-ansi-tarball.sh
# image was removed from source in v0.2.0

Source0:	http://registry.npmjs.org/ansi/-/ansi-%{version}.tgz
Source1:	https://raw.githubusercontent.com/kasicka/ansi.js/master/LICENSE
# https://github.com/TooTallNate/ansi.js/pull/23

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch:	%{nodejs_arches} noarch
%else
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel

%description
ansi.js is a module for Node.js that provides an easy-to-use API for writing
ANSI escape codes to Stream instances. ANSI escape codes are used to do fancy
things in a terminal window, like render text in colors, delete characters,
lines, the entire window, or hide and show the cursor, and lots more!

%prep
%setup -q -n package

cp -p %{SOURCE1} .

#fix perms in stuff that goes in %%doc
chmod 0644 examples/*.js examples/*/*

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ansi
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/ansi

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/ansi
%doc README.md examples
%license LICENSE

%changelog
* Mon Aug 10 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.0-2
- rebuilt

* Wed Jul 15 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.0-1
- New upstream release
- remove deprecated parts of spec
- add missing license
- changed Source

* Fri Sep 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- update to upstream release 0.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- new upstream release 0.2.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-8.1
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-7.1
- rebuild for missing npm(ansi) provides (RHBZ#968531)

* Fri May 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-7
- remove nonfree image

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-6
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.2-6
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-4
- fix permissions correctly

* Fri Jan 11 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-3
- fix permissions in example

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-2
- add missing build section
- fix incorrect summary

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.2-1
- New upstream release 0.1.2

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-1
- new upstream release 0.1.0

* Fri Mar 16 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package
