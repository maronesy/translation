# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 83 (printed ٨٢)."""

PAGE_NUMBER = 83
PRINTED_PAGE = "٨٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "(ونحو: مسلمي) عطف على قوله: «كقاض»[[١]]، يعني: تقدير الإعراب للاستثقال.",
     "en": "(And like: muslimiyya) is conjoined to his words “like qāḍin,” meaning: the estimation (taqdīr) of iʿrāb on account of heaviness (istithqāl)."},
    {"type": "matn",
     "ar": "قد يكون في الإعراب بالحركة، وقد يكون في الإعراب بالحروف نحو: «مسلمي»، بخلاف تقدير الإعراب للتعذر، فإنه مختص بالإعراب بالحركة.",
     "en": "It may occur in iʿrāb by a vowel (ḥaraka), and it may occur in iʿrāb by letters (ḥurūf), as in “muslimiyya” — unlike the estimation of iʿrāb on account of impossibility (taʿadhdhur), which is confined to iʿrāb by a vowel."},
    {"type": "matn",
     "ar": "(رفعا) يعني: تقدير الإعراب في نحو: «مسلمي»، إنما هو في حالة الرفع فقط دون النصب والجر، نحو: «جاءني مسلمي»،",
     "en": "(In the nominative — rafʿan) meaning: the estimation of iʿrāb in the like of “muslimiyya” occurs only in the state of the nominative, not the accusative (naṣb) or the genitive (jarr) — as in “muslimiyya came to me,”"},
    {"type": "matn",
     "ar": "فإن أصله «مسلموي» بسقوط النون بالإضافة، فاجتمع الواو والياء، والسابق منهما ساكن، فانقلبت الواو ياء، وأدغمت الياء في الياء، وكسر ما قبل الياء، فلم يبق علامة الرفع، التي هي الواو في اللفظ،",
     "en": "for its origin is “muslimuwī”: with the nūn dropping through the genitive construction (iḍāfa), the wāw and the yāʾ came together, the former of them being quiescent (sākin); so the wāw was converted into a yāʾ, the yāʾ was assimilated into the [other] yāʾ, and what precedes the yāʾ was given a kasra; thus the sign of the nominative — which is the wāw — no longer remained in the utterance,"},
    {"type": "matn",
     "ar": "فصار الإعراب في حالة الرفع تقديريا، بخلاف حالتي النصب والجر، فإن الإدغام لا يخرج الياء عن حقيقتها، فإن الياء المدغمة أيضا ياء.",
     "en": "so the iʿrāb in the state of the nominative became estimated (taqdīrī), unlike the two states of the accusative and genitive, for assimilation does not remove the yāʾ from its reality, since the assimilated yāʾ is likewise a yāʾ."},
    {"type": "matn",
     "ar": "وقد يكون الإعراب بالحروف تقديريا[[٢]] في الأحوال الثلاث[[٣]] في مثل: «جاءني أبو القوم»، و«رأيت أبا القوم»، و«مررت بأبي القوم»،",
     "en": "And iʿrāb by letters may be estimated in [all] three states, as in: “the chief of the people (abū l-qawm) came to me,” “I saw the chief of the people (abā l-qawm),” and “I passed by the chief of the people (bi-abī l-qawm)” —"},
    {"type": "matn",
     "ar": "فإنه لما سقطت حروف الإعراب عن اللفظ بالتقاء الساكنين لم يبق الإعراب لفظا، بل صار تقديريا.",
     "en": "for when the letters of iʿrāb dropped from the utterance through the meeting of two quiescents (iltiqāʾ al-sākinayn), the iʿrāb no longer remained in the utterance, but rather became estimated."},
    {"type": "matn",
     "ar": "(واللفظي) أي: الإعراب المتلفظ به (فيما عداه) يعني: فيما عدا ما ذكر مما تعذر فيه الإعراب، أو استثقل[[٤]].",
     "en": "(And the pronounced [iʿrāb] — al-lafẓī) that is: the iʿrāb that is actually uttered (in whatever is other than it — fīmā ʿadāhu) meaning: in whatever is other than what has been mentioned, wherein iʿrāb was impossible or was found heavy."},

    {"type": "section", "ar": "[ الممنوع من الصرف ]",
     "en": "The Diptote (al-Mamnūʿ min al-Ṣarf)"},

    {"type": "matn",
     "ar": "ولما ذكر في تفصيل المعرب المنصرف وغير المنصرف، وكان غير المنصرف أقل[[٥]] من المنصرف، وبمعرفته يعرف المنصرف على قياس الإعراب التقديري واللفظي",
     "en": "Since, in detailing the declinable (muʿrab), he mentioned the triptote (al-munṣarif) and the diptote (ghayr al-munṣarif), and since the diptote is fewer [in instances] than the triptote, and by knowing it the triptote is known — on the analogy of estimated and pronounced iʿrāb —"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "مرفوعا أو منصوبا لا على قوله: «قاض»؛ إذ لو قصد حينئذ بلفظ «نحو» تمثيل تقدير الإعراب كان مستدركا لإفادة الكاف إياه.",
     "en": "[It is] nominative or accusative — not [conjoined] to his words “qāḍin”; for if by the expression “naḥwu” (the like of) the illustration of estimated iʿrāb had then been intended, it would have been redundant, since the kāf [of “ka-qāḍin”] already conveys that."},
    {"type": "pair",
     "ar": "ولو قصد به كون اللفظ جمعا سالما بالواو والنون مضافا إلى ياء المتكلم لم يحتج أيضا إلى ذكره؛ إذ ليس المقصود في التمثيلات خصوصية المذكورات، بل يراد المذكورات وأخواتها، ولهذا لم يجمع بين الكاف ونحوها.",
     "en": "And if by it were intended [to show] the word being a sound plural with wāw and nūn annexed to the pronoun of the speaker, mentioning it would likewise not have been necessary; for what is aimed at in illustrations is not the particularity of the items cited, but rather the items cited and their like are what is intended — which is why the kāf and “naḥwu” were not combined [in a single example]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الفاضل الهندي: إن تلفظ الإعراب في «مسلمي» بعد الإعلال متعذر وقبله مستثقل كما في «عصا»، لكن المؤثر في التقدير في «عصا» ما بعد الإعلال من التعذر، وفي «مسلمي» ما قبله من الاستثقال؛",
     "en": "Al-Fāḍil al-Hindī said: the uttering of iʿrāb in “muslimiyya” is impossible after the mutation (iʿlāl) and heavy before it — as in “ʿaṣā”; yet what causes the estimation in “ʿaṣā” is [the state] after the mutation — namely the impossibility — whereas in “muslimiyya” it is [the state] before it, namely the heaviness;"},
    {"type": "pair",
     "ar": "لأن إعرابه بالواو، وثقله يوجب تقديرها، بخلاف «عصا»، فإن إعرابه بالحركة، وثقله يوجب إبدال الحرف لا الإسكان وتقدير الحركة.",
     "en": "because its iʿrāb is by the wāw, and its heaviness necessitates estimating it — unlike “ʿaṣā,” whose iʿrāb is by a vowel, and whose heaviness necessitates substituting the letter, not rendering [it] quiescent and estimating the vowel."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وضابطه: ما إذا كان الإعراب مدة ولاقى ساكنا.",
     "en": "Its criterion is: when the iʿrāb is a long vowel (madda) and it meets a quiescent."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "للاستثقال. وضابطه: ما إذا كان الإعراب مدة ولاقى ساكنا، نحو: «والمقيمي الصلاة» بجر «الصلاة» ونصبها،",
     "en": "[This is] on account of heaviness. Its criterion is: when the iʿrāb is a long vowel and it meets a quiescent, as in “wa-l-muqīmī l-ṣalāti” — reading “al-ṣalāt” in the genitive or the accusative;"},
    {"type": "pair",
     "ar": "فخرج نحو: «مصطفو القوم» والمثنى الغير المرفوع، فإن إعرابه لا يكون مدة أصلا.",
     "en": "thereby excluding the like of “muṣṭafū l-qawm” and the non-nominative dual, for their iʿrāb is never a long vowel to begin with."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: أقل أفرادا منه؛ لأن شرائطه ومعانداته أكثر، وأنه كلما كان الشيء أكثر شروطا كان أقل أفرادا.",
     "en": "That is: fewer in individual instances than it, because its conditions and its counter-factors are more numerous; and the more numerous a thing’s conditions are, the fewer its instances."},
]
