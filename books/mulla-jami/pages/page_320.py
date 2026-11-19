# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 320 (printed ٣١٩)."""

PAGE_NUMBER = 320
PRINTED_PAGE = "٣١٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وإنما كان» at the foot of PDF p. 319.
    {"type": "matn",
     "ar": "ملحقا بالصحيح؛ لأن حرف العلة بعد السكون لا يثقل عليها الحركة، لمعارضة خفة السكون ثقل الحركة،",
     "en": "…assimilated to the sound noun because a weak letter after a quiescent letter is not burdened by a vowel, since the lightness of the quiescence offsets the heaviness of the vowel;"},
    {"type": "matn",
     "ar": "ولأن حرف العلة بعد السكون مثلها بعد السكوت في الوقوع بعد استراحة اللسان، ولا يثقل عليها الحركة بعد السكوت -يعني: في الابتداء- كذا بعد السكون",
     "en": "and because a weak letter after a quiescent letter is like one after silence, in that it comes after the tongue has rested; and a vowel does not burden it after silence—that is, at the beginning [of speech]—and likewise after a quiescent letter;"},
    {"type": "matn",
     "ar": "(إلى ياء المتكلم، كسر آخره) للتناسب مثل: ثوبي وداري في الصحيح، و«ظبي ودلوي» في الملحق به",
     "en": "(to the yāʾ of the first person, its last letter takes kasra) for congruence, as in “thawbī” (my garment) and “dārī” (my house) for the sound noun, and “ẓabyī” (my gazelle) and “dalwī” (my bucket) for the assimilated noun;"},
    {"type": "matn",
     "ar": "(والياء مفتوحة أو ساكنة) وقد اختلف في أن أيهما الأصل[[١]]، والصحيح أنه الفتح؛",
     "en": "(and the yāʾ takes fatḥa or is quiescent). There is disagreement over which of the two is original; the correct view is that it is the fatḥa,"},
    {"type": "matn",
     "ar": "إذ الأصل في الكلمة التي على حرف واحد هو الحركة؛ لئلا يلزم الابتداء بالساكن حقيقة[[٢]] أو حكما[[٣]]، والأصل فيما يبنى الحركة الفتح، والسكون إنما هو عارض للتخفيف.",
     "en": "since the default for a word consisting of a single letter is a vowel, lest one be forced to begin with a quiescent letter, actually or virtually; the default vowel for what is indeclinable is fatḥa, and quiescence is only incidental, for lightening."},
    {"type": "matn",
     "ar": "(فإن كان آخره) أي: آخر الاسم المضاف إلى ياء المتكلم (ألفا[[٤]] تثبت) أي: الألف على اللغة الفصيحة لعدم موجب الانقلاب نحو: «عصاي ورحاي»",
     "en": "(If its last letter)—that is, the last letter of the noun annexed to the yāʾ of the first person—(is an alif, it remains), that is, the alif, in the eloquent dialect, since nothing requires its change, as in “ʿaṣāya” (my staff) and “raḥāya” (my millstone);"},
    {"type": "matn",
     "ar": "(وهذيل) وهي قبيلة من العرب (تقلبها) أي: الألف حال كونها (لغير التثنية ياء) لمشاكلة ياء المتكلم[[٥]]، وتدغم في الياء مثل: «عصي ورحي»،",
     "en": "(and Hudhayl)—an Arab tribe—(change it), that is, the alif, when it is (not that of the dual, into yāʾ), to match the yāʾ of the first person, and it is assimilated into the yāʾ, as in “ʿaṣayya” and “raḥayya”;"},
    {"type": "matn",
     "ar": "ولا تقلب ألف التثنية[[٦]] كـ«غلاماي»؛ لالتباس المرفوع بغيره بسبب القلب.",
     "en": "but the alif of the dual is not changed, as in “ghulāmāya” (my two slaves), because the change would confuse the nominative with the other cases."},
    {"type": "matn",
     "ar": "(وإن كان) آخر الاسم المضاف إلى ياء المتكلم (ياء أدغمت) في ياء المتكلم لاجتماع المثلين فيما هو كالكلمة الواحدة،",
     "en": "(If) the last letter of the noun annexed to the yāʾ of the first person (is a yāʾ, it is assimilated) into the yāʾ of the first person, because two like letters meet in what is as a single word,"},
    {"type": "matn",
     "ar": "مثل: «مسلمين» إذا أضيف إلى ياء المتكلم، وأسقط النون للإضافة، وأدغم الياء في الياء، فصار «مسلمي».",
     "en": "as with “muslimīna” when it is annexed to the yāʾ of the first person: the nūn is dropped for annexation and the yāʾ is assimilated into the yāʾ, so that it becomes “muslimiyya.”"},
    {"type": "matn",
     "ar": "(وإن كان) آخره (واوا قلبت) الواو (ياء) لاجتماع الواو والياء، والأولى ساكنة،",
     "en": "(If) its last letter (is a wāw, it is changed), the wāw, (into yāʾ), because wāw and yāʾ meet and the first is quiescent,"},
    {"type": "matn",
     "ar": "مثل: «مسلمون» إذا أضيف إلى ياء المتكلم، قلبت واوه ياء (وأدغمت) الياء في الياء",
     "en": "as with “muslimūna” when it is annexed to the yāʾ of the first person: its wāw is changed into yāʾ (and assimilated), the yāʾ into the yāʾ…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وفي تقديم مفتوحة إشعار باختيار أن الأصل الفتحة، لكن قوله: وفتحت للساكنين ظاهر في أن السكون هو الأصل، فليتأمل.",
     "en": "Putting “takes fatḥa” first suggests that he prefers the view that fatḥa is original; but his words “and it takes fatḥa because of the two quiescent letters” plainly indicate that quiescence is original. Let this be considered."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيما إذا كانت في صدر الكلام.",
     "en": "That is, when it stands at the beginning of the utterance."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: print reads «لاستقالها»; «لاستقلالها» (because of its independence) appears intended; transcribed as printed.
    {"type": "pair",
     "ar": "فيما إذا لم تكن في الصدر؛ لأنها لاستقالها في حكم الابتداء بها.",
     "en": "That is, when it is not at the beginning; because, owing to its independence, it counts as being begun with."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: إن لم يكن الاسم صحيحا ولا ملحقا به فإن كان إلى آخره.",
     "en": "That is: if the noun is neither sound nor assimilated to the sound, then if [its last letter] is … to the end."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن مشاكلها حركة الكسرة، فلما تعذر التزم الياء التي هي أختها.",
     "en": "Because what matches it is the kasra vowel; since that was impossible, the yāʾ, which is its sister, was adopted."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قيل: كان الواجب على هذا ألا يقلب واو الجمع ياء للالتباس.",
     "en": "It has been said: on this basis the wāw of the plural ought not to be changed into yāʾ, because of the confusion."},
    {"type": "pair",
     "ar": "وأجيب عنه: بأن أصل الألف عدم القلب قبل الياء لخفتها.",
     "en": "The answer given: the default for alif is not to be changed before yāʾ, owing to its lightness."},
    {"type": "pair",
     "ar": "وإنما جوز هذيل القلب لأمر استحساني لا يوجب القلب عند الجمع بخلاف قلب الواو في مسلمي،",
     "en": "Hudhayl permitted the change only for a reason of preference (istiḥsān) that does not require the change in the plural; unlike the change of the wāw in “muslimiyya,”"},
    {"type": "pair",
     "ar": "فإنه لأمر يوجب القلب عند الجمع، وهو اجتماع الواو والياء وسكون أولهما، ولا يترك الأمر المطرد اللازم لالتباس يعرض في بعض المواضع.",
     "en": "which is for a reason that requires the change in the plural, namely the meeting of wāw and yāʾ with the first quiescent; and a regular, binding rule is not abandoned because of a confusion that arises in some places."},
]
