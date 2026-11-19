# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 321 (printed ٣٢٠)."""

PAGE_NUMBER = 321
PRINTED_PAGE = "٣٢٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وأدغمت) الياء في الياء» at the foot of PDF p. 320 (mid-sentence).
    {"type": "matn",
     "ar": "وكسر ما قبلها؛ لأنها لما انقلبت ياء ساكنة يوجب بقاء الضمة[[١]] قبلها تغيرها[[٢]]، فحركت بالحركة المناسبة لها فقيل: «مسلمي».",
     "en": "…and what precedes it was given kasra; for once it had turned into a quiescent yāʾ, keeping the ḍamma before it would require its alteration, so it was vowelled with the vowel that suits it, and “muslimiyya” (my Muslims) was said."},
    {"type": "matn",
     "ar": "وإن كان قبل الياء أو الواو فتحة بقي ما قبلها مفتوحا كقولك في مسلمين: «مسلمي»، وفي مصطفون: «مصطفي» لخفة الفتحة.",
     "en": "If a fatḥa precedes the yāʾ or the wāw, what precedes it remains with fatḥa, as when you say for “muslimayni” (two Muslims) “muslimayya,” and for “muṣṭafawna” (the chosen ones) “muṣṭafayya,” because of the lightness of the fatḥa."},
    {"type": "matn",
     "ar": "(وفتحت الياء) أي: ياء المتكلم في الصور الثلاث[[٣]] (للساكنين[[٤]]) أي: للزوم التقاء الساكنين إن لم تتحرك، واختير الفتحة لخفتها[[٥]].",
     "en": "(And the yāʾ is given fatḥa), that is, the yāʾ of the speaker in the three cases, (because of the two quiescent letters), that is, because a meeting of two quiescent letters would necessarily result if it were not vowelled; and the fatḥa was chosen for its lightness."},
    {"type": "matn",
     "ar": "(وأما الأسماء الستة) التي مر البحث عنها[[٦]] مضافة إلى غير ياء المتكلم (فـ«أخي وأبي»[[٧]]) أي: فالحال في «أخ وأب»[[٨]] منها -إذا أضيفا إلى ياء المتكلم- أن يقال:",
     "en": "(As for the six nouns), whose discussion when annexed to something other than the yāʾ of the speaker has already passed, (they are “akhī” and “abī”), that is, the case with “akh” and “ab” among them, when they are annexed to the yāʾ of the speaker, is that one says:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأن الياء الساكنة إذا كانت قبلها ضمة تقلب واوا.",
     "en": "Because a quiescent yāʾ preceded by a ḍamma is turned into a wāw."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: قلب الضمة كسرة بعد قلب الواو ياء واجب إذا لم يؤد إلى اللبس.",
     "en": "Shaykh al-Raḍī said: turning the ḍamma into a kasra after the wāw has been turned into a yāʾ is obligatory when it does not lead to ambiguity."},
    {"type": "pair",
     "ar": "أما إذا أدى إلى لبس وزن بوزن فأنت مخير في إبقائها وقلبها كسرة نحو: لي في جمع ألوي إذ يشبه فعل بفعل.",
     "en": "When it does lead to one pattern being confused with another, you may choose between keeping it and turning it into a kasra, as with “luyy” as the plural of “alwā,” since [otherwise] the pattern fuʿl would resemble the pattern fiʿl."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: ذلك الإيجاب فيما لم يلزم الالتباس.",
     "en": "Shaykh al-Raḍī said: that requirement holds where no confusion results."},
    {"type": "pair",
     "ar": "أما فيما يلزم فتبقى الضمة كما في لي جمع ألوى على أفعل الصفة أبقى الضمة لئلا يلتبس فعل بفعل.",
     "en": "Where confusion would result, the ḍamma remains, as in “luyy,” plural of “alwā” on the adjectival pattern afʿal: he kept the ḍamma lest the pattern fuʿl be confused with fiʿl."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: print reads «لأجراء» with hamza above the alif; the sense requires «لإجراء»; transcribed as printed.
    {"type": "pair",
     "ar": "قد جاء الياء ساكنا مع الألف في قراءة نافع: ﴿محياي ومماتي﴾، إما لأجراء الوصل مجرى الوقف،",
     "en": "The yāʾ has occurred quiescent after the alif in the reading of Nāfiʿ: “maḥyāy wa-mamātī” (my life and my death), either from treating continuous speech as a pause,"},
    {"type": "pair",
     "ar": "أو لأن الألف أكثر مدا من أخويه فهو يقوم مقام الحركة من جهة صحة الاعتماد عليه،",
     "en": "or because the alif has more prolongation than its two sisters [wāw and yāʾ], so it takes the place of a vowel in that one can properly rest upon it;"},
    {"type": "pair",
     "ar": "ومع هذا فهو عند النحويين ضعيف، كذا ذكره الشيخ الرضي.",
     "en": "even so, it is weak according to the grammarians; so Shaykh al-Raḍī mentioned."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: وقراءة محياى ومماتى بسكون الياء عند النحويين ضعيف.",
     "en": "Shaykh al-Raḍī said: the reading “maḥyāy wa-mamātī” with a quiescent yāʾ is weak according to the grammarians."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الظاهر أن اختيار الفتحة لأنها الحركة التي كانت للياء.",
     "en": "What appears is that the fatḥa was chosen because it is the vowel that the yāʾ [originally] had."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا بمنزلة الاستثناء من قوله: فإن كان آخره ألفا تثبت، وإن كان ياء أدغمت، وإن كان واو قلبت ياء وأدغمت،",
     "en": "This stands as an exception to his words: “If its end is an alif, it remains; if a yāʾ, it is assimilated; and if a wāw, it is turned into a yāʾ and assimilated.”"},
    {"type": "pair",
     "ar": "فإن كان في آخره هذه الأسماء الحروف الثلاثة في الأحوال الثلاث إذا أضيف إلى غير ياء المتكلم ففي الإضافة إلى الياء يجب أن يكون على الأحكام المذكورة في الحروف الثلاث، فاستثناها ببيان حكمها،",
     "en": "For since these nouns have the three letters at their end in the three states when annexed to something other than the yāʾ of the speaker, in annexation to the yāʾ they ought to follow the rules stated for the three letters; so he excepted them by setting out their rule."},
    {"type": "pair",
     "ar": "أو بمنزلة الاستثناء من إضافة الاسم الصحيح؛ لأنها تحذف أعجازها نسيا منسيا أسماء صحيحة مع أن بعضها ليس كالأسماء الصحيحة وهو في وأخي وأبي على ما أجازها المبرد،",
     "en": "Or it stands as an exception to the annexation of the sound noun; for with their final parts elided and wholly forgotten they are sound nouns, although some of them are not like sound nouns, namely “fī,” and “akhī” and “abī” as al-Mubarrad allowed them;"},
    {"type": "pair",
     "ar": "ويتجه حينئذ أنه ينبغي أن يتعرض بمجرد أخي وأبي وفي، والتعرض بالباقي عار عن الفائدة.",
     "en": "on this view the objection arises that he should have dealt only with “akhī,” “abī” and “fī,” and that dealing with the rest is devoid of benefit."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قدم الأخ لأنها أبعد عن خلاف المبرد، وأوضح في هذا الحكم،",
     "en": "He put “akh” first because it is further from al-Mubarrad’s dissent and clearer in this rule;"},
    {"type": "pair",
     "ar": "كيف ولم يستعمل أخي بالتشديد، وإنما أجازه المبرد حملا على ما ورد من أبي كما صرح به الشارح،",
     "en": "how not, when “akhiyya” with doubling is not used, and al-Mubarrad allowed it only by analogy with what is attested of “abiyya,” as the commentator stated explicitly."},
    {"type": "pair",
     "ar": "ومنهم من قال: قدم الأخ لتقديمه في قوله تعالى: ﴿يوم يفر المرء من أخيه وأمه وأبيه. وصاحبته وبنيه﴾ (عبس: ٣٤-٣٦).",
     "en": "Some said: he put “akh” first because it comes first in the words of the Exalted: “On the Day a man flees from his brother, and his mother and his father, and his wife and his sons” (Qurʾān, Sūrat ʿAbasa 80:34–36)."},
    {"type": "pair",
     "ar": "وأنا أقضي منه العجب، وأراه أعجب من كل أعجب.",
     "en": "I am astonished at this, and I find it more astonishing than anything astonishing."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: print reads «أو فيقال» at the head of the note; transcribed as printed.
    {"type": "pair",
     "ar": "أو فيقال في إضافة بعضها إلى ياء المتكلم أخي وأبي.",
     "en": "Or: so one says, in annexing some of them to the yāʾ of the speaker, “akhī” and “abī.”"},
    # REVIEW: «حمى» as printed (the matn's form is presumably «حمي»); transcribed as printed.
    {"type": "pair",
     "ar": "وعلى هذا يكون عطف قوله: وأجاز المبرد، وعطف قوله: وتقول حمى عليه عطف فعلية على فعلية.",
     "en": "On this reading, the conjunction of his words “and al-Mubarrad allowed” and of his words “and you say ḥamī” to it is the conjunction of a verbal clause to a verbal clause."},
    {"type": "pair",
     "ar": "وأما على ظاهر توجيه الشرح، فيكون عطف فعلية على اسمية.",
     "en": "On the apparent sense of the commentary’s construal, however, it is the conjunction of a verbal clause to a nominal clause."},
]
