# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 298 (printed ٢٩٧)."""

PAGE_NUMBER = 298
PRINTED_PAGE = "٢٩٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وهذا القيد يغني عن الأول (مبني على» from the foot of PDF p. 297.
    {"type": "matn",
     "ar": "الفتح) حملا على المنعوت، لمكان الاتحاد[[١]] بينهما والاتصال وتوجه النفي إليه، أي: إلى النعت حقيقة،",
     "en": "…the fatḥa), by construction on the qualified noun (manʿūt), because of the identity between them, their adjacency, and the negation’s being directed to it—that is, to the qualifier—in reality."},
    {"type": "matn",
     "ar": "و«المبني» في قوله: «ونعت المبني» إشارة إلى ما بني على الفتح بالأصالة لا بالتبعية، فإنه المذكور سابقا،",
     "en": "“Al-mabnī” in his words “the qualifier of the indeclinable” refers to what is indeclinable on the fatḥa in its own right, not as a dependent, for that is what was mentioned earlier."},
    {"type": "matn",
     "ar": "فلا يرد أنه إذا كرر المبني ويبنى على الفتح ثم جيء بنعت لا يجوز بناؤه مثل: «لا ماء ماء باردا»",
     "en": "So no objection arises that, when the indeclinable is repeated and [the repetition] is made indeclinable on the fatḥa, and then a qualifier is brought, its indeclinability is not permitted, as in “lā māʾa māʾa bāridan” (there is no water, cold water),"},
    {"type": "matn",
     "ar": "مع أنه يصدق عليه أنه «نعت المبني الأول مفردا يليه»،",
     "en": "although it is true of it that it is “the first qualifier of the indeclinable, single, following it”;"},
    {"type": "matn",
     "ar": "فإن «باردا» في هذا المثال نعت للتابع لا المتبوع، كما هو الظاهر، ولو جعل نعتا للمتبوع فليس مما يليه، لتوسط التابع بينهما",
     "en": "for “bāridan” in this example qualifies the dependent, not the antecedent, as is evident; and were it made a qualifier of the antecedent, it would not be among what follows it, since the dependent intervenes between them."},
    {"type": "matn",
     "ar": "(ومعرب)؛ لأن الأصل في التابع تبعيتها لمتبوعاتها في الإعراب دون البناء",
     "en": "(And declinable), because the default for dependents is that they follow their antecedents in inflection, not in indeclinability—"},
    {"type": "matn",
     "ar": "(رفعا) حملا على محله البعيد (ونصبا[[٢]]) حملا على اللفظ أو على محله القريب",
     "en": "(in the nominative), by construction on its far position, (and in the accusative), by construction on the form or on its near position,"},
    {"type": "matn",
     "ar": "(نحو: «لا رجل ظريف) بالفتح (وظريف) بالرفع (وظريفا») بالنصب.",
     "en": "(as in “lā rajula ẓarīfa”) with the fatḥa, (“ẓarīfun”) with the nominative, (and “ẓarīfan”) with the accusative (there is no refined man)."},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن النعت كذلك (فالإعراب) أي: فحكمه الإعراب لا غير[[٣]]،",
     "en": "(Otherwise), that is, if the qualifier is not so, (then inflection), that is, its rule is inflection and nothing else:"},
    {"type": "matn",
     "ar": "رفعا حملا على المحل البعيد، أو نصبا حملا على اللفظ أو على المحل القريب، وقد مرت أمثلته في بيان فوائد القيود.",
     "en": "the nominative by construction on the far position, or the accusative by construction on the form or on the near position; its examples have already passed in the account of the purposes of the restrictions."},
    {"type": "matn",
     "ar": "(والعطف) على اسم «لا» المبني إذا كان المعطوف نكرة بلا تكرير لا في المعطوف،",
     "en": "(Conjunction) to the indeclinable noun of “lā,” when the conjoined noun is indefinite, without repetition of lā in the conjoined—"},
    {"type": "matn",
     "ar": "فإنه إذا كان المعطوف معرفة وجب رفعه نحو: «لا غلام لك والفرس».",
     "en": "for when the conjoined noun is definite, its nominative is obligatory, as in “lā ghulāma laka wa-l-farasu” (you have no slave, nor the horse)."},
    {"type": "matn",
     "ar": "وإذا كان «لا» مكررا في المعطوف فحكمه ما علم في قوله: «لا حول ولا قوة» فيما سبق",
     "en": "When “lā” is repeated in the conjoined, its rule is what was learned from his words “lā ḥawla wa-lā quwwata” above—"},
    {"type": "matn",
     "ar": "بأن يحمل (على اللفظ) أي: على لفظ اسم «لا» المبني، ويجعل منصوبا (و) بأن يحمل (على المحل) ويجعل مرفوعا[[٤]] (جائز)",
     "en": "that it be construed (on the form), that is, on the form of the indeclinable noun of “lā,” and made accusative, (and) that it be construed (on the position) and made nominative, (is permitted);"},
    {"type": "matn",
     "ar": "ولا يجوز فيه البناء، لمكان الفصل بالعاطف، ولم يجعل في حكم المتصل، لمظنة الفصل بـ«لا» المؤكدة؛",
     "en": "indeclinability is not permitted in it, because of the separation by the conjunction; nor was it treated as adjacent, since separation by an emphatic “lā” is to be presumed,"},
    {"type": "matn",
     "ar": "إذ المعطوف على المنفي تزاد فيه «لا» كثيرا نحو: «لا حول ولا قوة»،",
     "en": "for “lā” is often added to what is conjoined to a negated noun, as in “lā ḥawla wa-lā quwwata”—"},
    {"type": "matn",
     "ar": "(مثل: «لا أب وابنا وابن») في قول الشاعر:",
     "en": "(as in “lā aba wa-bnan” and “wa-bnun”), in the poet’s saying:"},
    {"type": "verse",
     "ar": "ولا أب وابنا مثل مروان وابنه          إذا هو بالمجد ارتدى وتأزرا",
     "en": "There is no father and son like Marwān and his son, when he has donned glory as cloak and wrapper."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: لثبوت الاتحاد ذاتا، والاتصال لفظا. وتوجه النفي إليه حقيقة؛",
     "en": "That is, because of the established identity in essence, adjacency in wording, and the negation’s being directed to it in reality;"},
    {"type": "pair",
     "ar": "لأنك إذا قلت: لا رجل ظريف، أي: كيسا، فكأنك قلت: لا ظريف.",
     "en": "for when you say “lā rajula ẓarīfa,” that is, clever, it is as if you said “there is none refined.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "مصدران نوعيان. والقول بأنه منصوب بنزع الخافض ضعيف؛ لأنه سماعي إلا في أن وأن.",
     "en": "[Rafʿan and naṣban are] two verbal nouns of kind (maṣdarān nawʿiyyān). The view that it is accusative through removal of the preposition (nazʿ al-khāfiḍ) is weak, since that depends on attested usage except with “an” and “anna.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى أن يقدر: فيجب الإعراب.",
     "en": "It is better to supply: “then inflection is obligatory.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: «مضي الخبر» clearly printed (as in fn. 2 of PDF p. 296); its exact sense is unclear.
    {"type": "pair",
     "ar": "القياس مضي الخبر.",
     "en": "The analogical rule is the predicate’s “passing” (muḍiyy al-khabar)."},
]
