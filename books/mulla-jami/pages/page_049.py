# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 49 (printed ٤٨)."""

PAGE_NUMBER = 49
PRINTED_PAGE = "٤٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "اعلم أن كلام المصنف ظاهر في أن نحو: «ضربت زيدا قائما»[[١]] بمجموعه كلام،",
     "en": "Know that the author’s words are apparent in indicating that [an expression] such as “I struck Zayd standing (ḍarabtu Zaydan qāʾiman)” is, in its totality, a speech (kalām),"},
    {"type": "matn",
     "ar": "بخلاف كلام صاحب المفصل، حيث قال: «الكلام: هو المركب من كلمتين أسندت إحداهما إلى الأخرى»، فإنه صريح في أن الكلام هو «ضربت» فقط، والمتعلقات خارجة عنه[[٢]].",
     "en": "unlike the words of the author of al-Mufaṣṣal [al-Zamakhsharī], where he said: “Speech is what is compounded of two words, one of which is predicated of the other,” for that is explicit in [holding] that the speech is “ḍarabtu (I struck)” alone, while the dependents (al-mutaʿalliqāt) lie outside it."},
    {"type": "matn",
     "ar": "ثم اعلم أن صاحب المفصل وصاحب اللباب ذهبا إلى ترادف الكلام والجملة، وكلام المصنف أيضا ينظر إلى ذلك[[٣]].",
     "en": "Then know that the author of al-Mufaṣṣal and the author of al-Lubāb both held that “speech (kalām)” and “sentence (jumla)” are synonymous, and the author’s words too incline toward that."},
    {"type": "matn",
     "ar": "فإنه قد اكتفى في تعريف الكلام بذكر الإسناد مطلقا، ولم يقيده بكونه مقصودا لذاته[[٤]].",
     "en": "For in defining speech he sufficed with mentioning predication unrestrictedly, and did not restrict it by its being intended for its own sake (maqṣūd li-dhātihi)."},
    {"type": "matn",
     "ar": "ومن جعله أخص[[٥]] من الجملة قيده به، فحينئذ يصدق الجملة على الجمل الخبرية[[٦]] الواقعة أخبارا، أو أوصافا[[٧]]، بخلاف الكلام[[٨]].",
     "en": "And whoever made it (speech) more specific than “sentence” restricted it by that [qualification]; in that case “sentence” applies truly to the declarative sentences occurring as predicates, or as adjectives, unlike “speech.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إنما قال: «ظاهر» لجواز أن يراد به: ما تضمن كلمتين فقط.",
     "en": "He said only “apparent” because it is possible that by it is meant: that which comprises two words alone."},
    {"type": "pair",
     "ar": "قيل: لا يخفى أنه لا يلزم عليه ارتكاب تحقق أفراد من الكلام في هذا التركيب.",
     "en": "It has been said: it is not hidden that this does not oblige him to admit the realization of [multiple] instances of speech within this composite."},
    {"type": "pair",
     "ar": "قلت: تحقق أفراد من الكلام في هذا التركيب كتحقق أفراد منه في «ضربت» أقوم «رجلا ضرب وهو قائم» على تعريف المفصل أيضا.",
     "en": "I say: the realization of instances of speech within this composite is like the realization of instances of it in “ḍarabtu” — which is more fitting [as an example] than “rajulan ḍaraba wa-huwa qāʾim (a man whom [someone] struck while he was standing)” — on the definition of al-Mufaṣṣal as well."},
    {"type": "pair",
     "ar": "ولا يذهب عليك أن خبر المبتدأ في قولنا: «زيد ضربت عمرا في داره» مجموع ما ذكر لا مجرد «ضربت».",
     "en": "And let it not escape you that the predicate of the subject (khabar al-mubtadaʾ) in our statement “Zayd — I struck ʿAmr in his house (Zaydun ḍarabtu ʿAmran fī dārihi)” is the totality of what was mentioned, not merely “ḍarabtu.”"},
    {"type": "pair",
     "ar": "وقد اتفقوا على أن خبر المبتدأ هنا جملة، فالكلام الذي هو مرادف الجملة عند صاحب المفصل يجب أن يكون مجموع ما جعل خبرا هنا.",
     "en": "They have agreed that the predicate of the subject here is a sentence; so the “speech” that is synonymous with “sentence” according to the author of al-Mufaṣṣal must be the totality of what is made a predicate here."},
    {"type": "pair",
     "ar": "وهكذا في الحال والصفة إذا كانتا جملتين، فينبغي أن يجعل عدول المصنف عدولا عن عبارة تعريفه لا عدولا عن مذهبه.",
     "en": "And likewise in the circumstantial qualifier (ḥāl) and the adjective (ṣifa) when they are both sentences. So the author’s departure ought to be reckoned a departure from the wording of his definition, not a departure from his doctrine."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: المعمولات غير الفاعل كالمفعول والحال. ويجوز فيها كسر اللام نظرا إلى أن الفعل عامل فيها، وفتحها نظرا إلى أن الحدث يتعلق بها، والمتعارف هو الأول.",
     "en": "That is: the governed elements (maʿmūlāt) other than the agent, such as the object (mafʿūl) and the circumstantial qualifier (ḥāl). It is permissible in it to read the lām with a kasra (al-mutaʿalliqāt) — considering that the verb governs them — and with a fatḥa (al-mutaʿallaqāt) — considering that the event (ḥadath) attaches to them; the customary reading is the first."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: يميل إلى الترادف. وفيه مجاز: فلا تغفل.",
     "en": "That is: it inclines toward [affirming] synonymy. And in it there is a figurative usage (majāz), so do not be heedless."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بيان لمعنى الإطلاق، أي: سواء كان الإسناد مقصودا لذاته أو لا.",
     "en": "An explanation of the meaning of “unrestrictedly (muṭlaqan),” that is: whether the predication be intended for its own sake or not."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: ومن اعتقد أن الكلام أخص من الجملة كالرضي والهندي قيد الإسناد بالأصلي المقصود لذاته.",
     "en": "That is: whoever held that “speech” is more specific than “sentence” — such as al-Raḍī and al-Hindī — restricted predication by the original predication intended for its own sake."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأولى: على الجمل الواقعة أخبارا من غير قيد الخبرية، وكأنه قيدها بها؛ لأن الإنشائية عنده لا يقع خبرا.",
     "en": "It would be preferable [to say]: “to the sentences occurring as predicates,” without the restriction “declarative”; yet it is as though he restricted them by it (the declarative), because the performative (inshāʾī), in his view, does not occur as a predicate."},
    {"type": "pair",
     "ar": "والواقعة خبرا مثل: «زيد اضربه» في تأويل «زيد» مقول في حقه «اضربه»، وبعد يتجه أن مادة افتراق الجملة عن الكلام لا يقتصر على الجملة الخبرية كما يوهمه البيان، بل من مادة الافتراق «اضربه» في «زيد اضربه» سواء كان خبرا أو متعلقا بالخبر.",
     "en": "And that which occurs as a predicate is like “Zaydun iḍribhu (Zayd, strike him),” construed as “Zayd — concerning whom ‘strike him’ is said”; and it then becomes clear that the point of divergence of “sentence” from “speech” is not confined to the declarative sentence, as [the author’s] exposition might suggest — rather “iḍribhu” in “Zaydun iḍribhu” is [also] among the points of divergence, whether it be a predicate or attached to the predicate."},
    {"type": "pair",
     "ar": "وقوله: «أخبارا أو أوصافا» يزاد عليه أو أحوالا أو جملة قسمية أو شروطا، فإن الحكم في الجزاء عند المصنف، وإلا لم يصح قوله: ولا يتأتى ذلك إلا في اسمين، ولا يكون تعريفه جامعا.",
     "en": "And his words “as predicates or as adjectives” — there should be added to them “or as circumstantial qualifiers, or an oath-sentence, or conditions”; for the [operative] judgement lies in the apodosis according to the author — otherwise his statement “that does not come about except in two nouns” would not be sound, nor would his definition be comprehensive (jāmiʿ)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أو جملة قسمية، فإن الكلام هو جواب القسم، والجملة القسمية للتأكيد أو شرطا، فإن الكلام هو الجزاء على زعمهم.",
     "en": "Or an oath-sentence (jumla qasamiyya), for the [operative] speech is the response to the oath (jawāb al-qasam), while the oath-sentence itself is for corroboration (taʾkīd); or [it may be] a condition, in which case the [operative] speech is the apodosis (jazāʾ), according to their claim."},
    {"type": "pair",
     "ar": "وأما على التحقيق فليس شيء من الشرط والجزاء كلاما، بل الكلام هو المجموع.",
     "en": "But upon [precise] verification, neither the protasis nor the apodosis is by itself a speech; rather the speech is the totality of both."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "فإنه لا يصدق عليها؛ لأن الإسناد فيها وسيلة لما هو المقصود بذاته.",
     "en": "For it (speech) does not apply truly to them, because predication in them is [merely] a means to what is intended for its own sake."},
]
