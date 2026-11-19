# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 319 (printed ٣١٨)."""

PAGE_NUMBER = 319
PRINTED_PAGE = "٣١٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # New sentence: the matn on PDF p. 318 ends «ففيهما خفاء.»
    {"type": "matn",
     "ar": "(و) يرد على قولهم: «ولا يضاف اسم مماثل للمضاف إليه في العموم والخصوص» (قولهم: «سعيد كرز» ونحوه)",
     "en": "(And) against their statement “a noun equivalent to the term annexed to in generality and particularity is not annexed” there is the objection of (their expression “Saʿīdu Kurzin” and the like);"},
    {"type": "matn",
     "ar": "فإن «سعيدا» و«كرزا» اسمان لمسمى واحد[[١]] كـ«ليث وأسد» مع أنه أضيف أحدهما إلى الآخر.",
     "en": "for “Saʿīd” and “Kurz” are two names for one named person, like “layth” and “asad,” and yet one of them has been annexed to the other."},
    {"type": "matn",
     "ar": "فأجيب عنه: بأنه (متأول) بحمل أحدهما على المدلول والآخر على اللفظ[[٢]]، فإنك إذا قلت: «جاءني سعيد كرز» كأنك قلت: جاءني مدلول هذا اللفظ[[٣]]،",
     "en": "The answer given is that it (is to be interpreted) by taking one of them as the thing denoted and the other as the expression; for when you say “jāʾanī Saʿīdu Kurzin,” it is as though you said: “there came to me what this expression denotes.”"},
    {"type": "matn",
     "ar": "ولم يقولوا: «كرز سعيد»؛ لأن قصدهم بالإضافة[[٤]] التوضيح، واللقب أوضح[[٥]] من الاسم غالبا[[٦]].",
     "en": "They did not say “Kurzu Saʿīdin,” because their purpose in the annexation is clarification, and the byname (laqab) is usually clearer than the name (ism)."},
    {"type": "matn",
     "ar": "(وإذا أضيف الاسم الصحيح) وهو في عرف النحاة[[٧]]: «ما ليس في آخره حرف علة»[[٨]] (أو الملحق به[[٩]]) وهو: «ما في آخره واو وياء ما قبلها ساكن»، وإنما كان",
     "en": "(When a sound noun (al-ism al-ṣaḥīḥ) is annexed)—which in the convention of the grammarians is “that at whose end there is no weak letter”—(or one assimilated to it), which is “that at whose end there is a wāw or yāʾ preceded by a quiescent letter”; it was only…"},

    {"type": "rule"},

    # ---------------- Footnote 10 continued from PDF p. 318 ----------------
    # Unnumbered: continues footnote ١٠ of PDF p. 318 («…مع قطع النظر عن تحققه في»).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "الذهن. وأما إذا أخذ من حيث إنه متحقق في الذهن فهو فرد من أفراد الشيء كمفهوم الإنسان بالنسبة إليه.",
     "en": "…the mind. But if it is taken as realized in the mind, then it is one of the individuals of “thing,” like the concept “human” in relation to it."},
    {"type": "pair",
     "ar": "وحينئذ يكون العين أعم منه.",
     "en": "In that case “ʿayn” is more general than it."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الوارد لا يخص هذا الحكم، بل كان متوجها على قوله: وشرطه بتجريد المضاف عن التعريف.",
     "en": "The objection is not specific to this rule; rather it was directed against his words “and its condition is that the annexed term be stripped of definiteness.”"},
    {"type": "pair",
     "ar": "وكأنه غفل المصنف عن وروده ثمة، فأخره إلى هنا.",
     "en": "It seems the author overlooked its arising there, and so deferred it to here."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فكأنك إذا قلت: جاءني سعيد كرز، قلت: جاءني مدلول هذا اللفظ يتبادر منه أنه أريد بالسعيد مطلق المدلول، وهو بعيد،",
     "en": "“So it is as though, when you say ‘jāʾanī Saʿīdu Kurzin,’ you said: ‘there came to me what this expression denotes’”—from this one immediately understands that by “Saʿīd” the denoted thing without qualification is meant, which is far-fetched;"},
    {"type": "pair",
     "ar": "بل الطريق في تنكير العلم أن يراد به المسمى به لا مطلق المدلول، فتأويل سعيد كرز مسمى بسعيد هو المسمى بكرز.",
     "en": "rather, the way to make a proper name indefinite is that by it is meant the one named by it, not the denoted thing without qualification; so the interpretation of “Saʿīdu Kurzin” is: one named Saʿīd who is the one named Kurz."},
    {"type": "pair",
     "ar": "والأظهر أن يراد بالكرز مدلوله دون اللفظ، ويؤول السعيد بمسمى به، فيكون من قبيل إضافة العام إلى الخاص لا إضافة المدلول إلى اللفظ، فاعرفه.",
     "en": "The more evident view is that by “Kurz” its denotatum is meant, not the expression, and “Saʿīd” is interpreted as “one named by it”; it is then of the kind in which the general is annexed to the particular, not the denotatum to the expression. Take note of this."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا دال هذا المدلول؛ لأن نسبة المجيء إلى الدال غير صحيح.",
     "en": "Not “the signifier of this denotatum,” because attributing coming to the signifier is not sound."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولأن اللقب يفيد تعيين الذات الذي يفيده الاسم مع زيادة مدح أو ذم، فإذا ذكر أولا يغني غناء الاسم،",
     "en": "And because the byname conveys the identification of the person that the name conveys, with the addition of praise or blame; so if it is mentioned first it does the work of the name."},
    {"type": "pair",
     "ar": "ولهذا لا يقدمون اللقب على الاسم، بل يؤخرون عنه، فيذكرونه على سبيل الاتباع بأن يكون عطف بيان أو على سبيل القطع مرفوعا أو منصوبا.",
     "en": "For this reason they do not put the byname before the name but after it, mentioning it as a dependent, as an explicative apposition (ʿaṭf bayān), or as detached (qaṭʿ), in the nominative or the accusative."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: جعل اللقب لكونه أوضح أحق بجعله موضحا لا أنه يجب أن يكون الموضح أوضح؛",
     "en": "That is: the byname, being clearer, is more entitled to be made the clarifying term—not that the clarifying term must be clearer;"},
    {"type": "pair",
     "ar": "إذ الموضح يكفي أن يجعل المدلول باجتماعه مع آخر أوضح سواء كان أوضح أو مساويا أو دونه،",
     "en": "for it suffices for the clarifying term that, in combination with another, it makes the denotatum clearer, whether it is itself clearer, equal, or less clear."},
    {"type": "pair",
     "ar": "فلا مانع من قبل التوضيح أن يقال: كرز سعيد إلا أنه لم يرد الاستعمال إلا على ما هو الأحق، ولا مانع من حيث القياس.",
     "en": "So, as far as clarification goes, nothing prevents saying “Kurzu Saʿīdin,” except that usage has come only with what is more entitled; and there is no bar from the standpoint of analogy."},
    {"type": "pair",
     "ar": "وكون اللقب أوضح إنما يظهر إذا لم يكن مشتركا، لكن الكرز مشترك.",
     "en": "The byname being clearer is evident only when it is not shared by several meanings; but “kurz” is equivocal (mushtarak)."},
    {"type": "pair",
     "ar": "في القاموس: الكرز اللئيم والحاذق. وابن علقمة وابن وبرة وابن جابر وآخر غير منسوب صحابيون هذا.",
     "en": "In al-Qāmūs: al-kurz is the base person and the skilled one; and Ibn ʿAlqama, Ibn Wabra, Ibn Jābir and another of unstated lineage are Companions [so named]. So much for this."},
    {"type": "pair",
     "ar": "والأظهر أن الكرز صار لقبا لهؤلاء من معنى الحاذق لا من معنى اللئيم.",
     "en": "The more evident view is that “Kurz” became a byname for these from the meaning “skilled,” not from the meaning “base.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "والمغلوب لا حكم له، فإن من عز بز أي: من غلب سلب.",
     "en": "What is outweighed has no standing, for “man ʿazza bazza,” that is: whoever prevails takes the spoils."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "احترز به عن عرف الصرفيين. ولهذا لم يقيد ببيان الملحق بعرفهم؛ إذ ليس لغيرهم فيه عرف.",
     "en": "By this he excludes the convention of the morphologists. For this reason he did not qualify his explanation of the assimilated noun by their convention, since others have no convention regarding it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وذلك لأن نظرهم في أحوال أواخر الكلم.",
     "en": "This is because their concern is with the states of the ends of words."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "معنى الإلحاق بالصحيح كون إعرابه بالحركات كالصحيح.",
     "en": "Being assimilated to the sound noun means that its inflection is by vowels, like the sound noun."},
]
