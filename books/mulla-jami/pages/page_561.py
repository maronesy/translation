# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 561 (printed ٥٦٠)."""

PAGE_NUMBER = 561
PRINTED_PAGE = "٥٦٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فصح أن يرفع المعطوف على اسمه،» at the foot of PDF p. 560.
    {"type": "matn",
     "ar": "حملا على محله (دون) «أن» (المفتوحة[[١]])، فإنه لم يجز العطف على محل اسمها بالرفع،",
     "en": "…by reference to its position; (not) “anna” (with fatḥa), for coordination in the nominative with the position of its noun is not permitted,"},
    {"type": "matn",
     "ar": "فإنها لما غيرت معنى الجملة لا يصح فرض عدمها.",
     "en": "since, as it alters the meaning of the sentence, it cannot be supposed non-existent."},
    {"type": "matn",
     "ar": "(ويشترط) في العطف على اسم «إن» المكسورة بالرفع (مضي الخبر) أي: ذكر خبرها قبل المعطوف (لفظا) مثل: «إن زيدا قائم وعمرو»",
     "en": "(And there is a condition) for coordination in the nominative with the noun of “inna” with kasra: (that the predicate has passed), that is, that its predicate is mentioned before the coordinated term, (in wording), as in “inna Zaydan qāʾimun wa-ʿAmrun”,"},
    {"type": "matn",
     "ar": "(أو تقديرا) مثل: «إن زيدا وعمرو قائم» أي: إن زيدا قائم وعمرو قائم؛",
     "en": "(or by implication), as in “inna Zaydan wa-ʿAmrun qāʾimun”, that is, “inna Zaydan qāʾimun wa-ʿAmrun qāʾimun”;"},
    {"type": "matn",
     "ar": "لأنه لو لم يمض الخبر قبله لا لفظا ولا تقديرا لزم اجتماع عاملين على إعراب واحد،",
     "en": "for if the predicate had not passed before it, neither in wording nor by implication, it would follow that two governing agents (ʿāmils) converge on one inflection,"},
    {"type": "matn",
     "ar": "مثل: «إن زيدا وعمرا ذاهبان»، فإنه لا شك أن «ذاهبان» خبر عن كل من المعطوف والمعطوف عليه.",
     "en": "as in “inna Zaydan wa-ʿAmran dhāhibāni (Zayd and ʿAmr are going)”, for there is no doubt that “dhāhibāni” is the predicate of both the coordinated term and the term it is coordinated with."},
    {"type": "matn",
     "ar": "فمن حيث إنه خبر عن اسم «إن» يكون العامل في رفعه «إن»، ومن حيث إنه خبر عن المعطوف على اسمه يكون العامل في رفعه الابتداء،",
     "en": "Insofar as it is the predicate of the noun of “inna”, what governs its nominative is “inna”; and insofar as it is the predicate of what is coordinated with its noun, what governs its nominative is inception (ibtidāʾ)."},
    {"type": "matn",
     "ar": "فلزم اجتماع عاملين، أعني: «إن» والابتداء على رفعه، وهو باطل[[٢]]،",
     "en": "So it follows that two governing agents, namely “inna” and inception, converge on its nominative, and that is invalid;"},
    {"type": "matn",
     "ar": "(خلافا للكوفيين)، فإنهم لا يشترطون في صحة هذا العطف مضي الخبر،",
     "en": "(in disagreement with the Kūfans), for they do not make the passing of the predicate a condition for the validity of this coordination,"},
    {"type": "matn",
     "ar": "فإن «إن» عندهم لا تعمل إلا في الاسم، والخبر مرفوع بالابتداء كما كان قبل دخول «إن» عليه. فلا يلزم اجتماع عاملين على إعراب واحد.",
     "en": "since for them “inna” governs only the noun, while the predicate is in the nominative by inception, as it was before “inna” entered upon it; so two governing agents do not converge on one inflection."},
    {"type": "matn",
     "ar": "(ولا أثر لكونه) أي: لكون اسم «إن»[[٣]] (مبنيا) في جواز العطف على محل اسم «إن» قبل مضي الخبر عند الجمهور،",
     "en": "(And its being), that is, the noun of “inna” being, (indeclinable has no effect) on the permissibility of coordination with the position of the noun of “inna” before the predicate has passed, according to the majority;"},
    {"type": "matn",
     "ar": "فلا يجوز عندهم «إنك وزيد ذاهبان»، كما أنه لا يجوز «إن زيدا وعمرو ذاهبان».",
     "en": "so for them “innaka wa-Zaydun dhāhibāni (you and Zayd are going)” is not permitted, just as “inna Zaydan wa-ʿAmrun dhāhibāni” is not permitted,"},
    {"type": "matn",
     "ar": "فإن المحذور المذكور مشترك بينهما (خلافا للمبرد والكسائي)، فإنهما يجوزان",
     "en": "for the impediment mentioned is common to both; (in disagreement with al-Mubarrad and al-Kisāʾī), for they permit…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "خلافا لبعض النحاة حيث جوزوا العطف في المفتوحة مطلقا.",
     "en": "In disagreement with some grammarians, who permitted coordination with the fatḥa form without qualification."},
    {"type": "pair",
     "ar": "وأما باقي التوابع فما سوى البدل كالمعطوف عند الجرمي والزجاج والفراء، وسكت غيرهم عنها، والكل عن البدل أيضا، والجواز هو القياس.",
     "en": "As for the remaining appositives (tawābiʿ), those other than the substitute (badal) are like the coordinated term according to al-Jarmī, al-Zajjāj and al-Farrāʾ; the others were silent about them, and all of them about the substitute as well; permissibility is what analogy requires."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأنه كاجتماع علتين مستقلتين على معمول واحد.",
     "en": "Because it is like two independent causes converging on one effect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي والكسائي مع باقي الكوفيين والفراء حكم بين الفريقين،",
     "en": "Shaykh al-Raḍī said: al-Kisāʾī [sides] with the rest of the Kūfans, while al-Farrāʾ arbitrated between the two parties,"},
    {"type": "pair",
     "ar": "فقال: إن كان اسم إن غير معرب لفظا جاز العطف على محله؛",
     "en": "saying: if the noun of inna is not declinable in its wording, coordination with its position is permitted,"},
    # REVIEW: printed «مستنكرا» (accusative) where «مستنكر» is expected as the predicate of «لأن كون…» — transcribed as printed.
    {"type": "pair",
     "ar": "لأن كون شيء واحد خبرا لاسمين متغايري الإعراب تغايرا ظاهرا مستنكرا، بخلاف كونه خبرا عن اسمين غير مخالفي الإعراب، فإنه ليس بتلك المثابة من الاستنكار،",
     "en": "because for one thing to be the predicate of two nouns whose inflections differ visibly is objectionable, unlike its being the predicate of two nouns that do not differ in inflection, which is not objectionable to that degree."},
    {"type": "pair",
     "ar": "وليس بناء عدم الجواز في «إن زيدا وعمرو قائمان» عنده على أنه يلزم اجتماع عاملين على معمول واحد في أثر واحد؛ لأن العامل في خبر إن عنده ما كان قبل دخولها،",
     "en": "For him, the impermissibility of “inna Zaydan wa-ʿAmrun qāʾimāni” is not based on its entailing two governing agents converging on one governed term in one effect, since for him what governs the predicate of inna is what governed it before inna entered."},
    {"type": "pair",
     "ar": "وما ذكره المصنف مسندا إلى المبرد والكسائي لا يوافق كتب النحو هذا،",
     "en": "What the author mentioned, attributing it to al-Mubarrad and al-Kisāʾī, does not agree with the books of grammar. So much for this."},
    {"type": "pair",
     "ar": "ولا يذهب عليك أن عبارة المصنف توهم خلاف المقصود حيث قال: خلافا للمبرد والكسائي في مثل: «أنك وزيد ذاهبان»؛",
     "en": "It should not escape you that the author’s wording suggests the opposite of what is intended, where he said: “in disagreement with al-Mubarrad and al-Kisāʾī in the like of ‘annaka wa-Zaydun dhāhibāni’”;"},
    {"type": "pair",
     "ar": "لأنه يشعر بأنهما لا يخالفان في انتفاء أثر البناء مطلقا، بل في قسم من البناء بأن يكون المبني هو المضمر،",
     "en": "for it suggests that the two do not dissent on the absence of any effect of indeclinability in general, but only in one kind of indeclinability, namely where the indeclinable term is a pronoun."},
    {"type": "pair",
     "ar": "فالواضح ترك \"في\" لينصرف الخلاف، والمثال كلاهما إلى الحكم.",
     "en": "The clearer course would have been to drop “fī”, so that both the disagreement and the example are directed to the ruling."},
]
