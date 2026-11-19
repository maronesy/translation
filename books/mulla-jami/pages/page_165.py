# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 165 (printed ١٦٤)."""

PAGE_NUMBER = 165
PRINTED_PAGE = "١٦٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "«زيد قام»، فإنه إذا قيل: «قام زيد» التبس المبتدأ بالفاعل، أو بالبدل[[١]] عن الفاعل إذا كان مثنى أو مجموعا[[٢]]،",
     "en": "…“Zaydun qāma”; for if “qāma Zaydun” were said, the mubtadaʾ would be confused with the fāʿil—or with the substitute (badal) for the fāʿil when it is dual or plural;"},
    {"type": "matn",
     "ar": "فإنه إذا قيل في مثل: «الزيدان قاما، والزيدون قاموا»: «وقاما الزيدان، وقاموا الزيدون» يحتمل أن يكون «الزيدان والزيدون» بدلا عن الفاعل، فالتبس المبتدأ به،",
     "en": "for if, in the like of “al-Zaydāni qāmā” and “al-Zaydūna qāmū,” one said “qāmā al-Zaydāni” and “qāmū al-Zaydūna,” it would be possible for “al-Zaydāni” and “al-Zaydūna” to be a substitute for the fāʿil, and so the mubtadaʾ would be confused with it;"},
    {"type": "matn",
     "ar": "أو بالفاعل على هذا التقدير أيضا على قول من يجوز كون الألف والواو حرفا دالا على تثنية الفاعل وجمعه كالتاء في «ضربت هند».",
     "en": "or with the fāʿil, on this supposition as well, according to the view of those who allow the alif and the wāw to be a particle indicating the dual and plural of the fāʿil, like the tāʾ in “ḍarabat Hindun” (Hind struck)."},

    {"type": "section", "ar": "[ وجوب تقديم الخبر ]",
     "en": "The Obligatory Fronting of the Khabar"},

    {"type": "matn",
     "ar": "(وإذا تضمن الخبر المفرد[[٣]]) أي: الذي ليس بجملة صورة، سواء كان بحسب الحقيقة جملة أو غير جملة (ما له صدر الكلام) أي: معنى وجب له صدر الكلام كالاستفهام[[٤]]",
     "en": "“And if the singular khabar”—that is, one that is not a sentence in form, whether in reality it is a sentence or not—“implicitly contains that which has the head of the utterance (ṣadr al-kalām),” that is, a meaning to which the head of the utterance is due, such as the interrogative,"},
    {"type": "matn",
     "ar": "(مثل: «أين زيد؟») فـ«زيد» مبتدأ، و«أين» اسم متضمن للاستفهام خبره، وهو ظرف،",
     "en": "“as in: ‘Where is Zayd?’ (ayna Zaydun)”: “Zayd” is the mubtadaʾ, and “ayna,” a noun implicitly containing the interrogative, is its khabar; it is an adverb (ẓarf)."},
    {"type": "matn",
     "ar": "فإن قدر بفعل كان الخبر جملة حقيقة ومفردا صورة، وإن قدر باسم الفاعل كان مفردا صورة وحقيقة. وعلى التقديرين ليس بجملة صورة.",
     "en": "If it is construed with [an implied] verb, the khabar is a sentence in reality and singular in form; if it is construed with an active participle (ism al-fāʿil), it is singular both in form and in reality. On either construal it is not a sentence in form."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «زيد أين أبوه؟»؛ إذ لا يبطل بتأخيره صدارة ما له صدر الكلام لتصدره في جملته[[٥]].",
     "en": "By it he excluded the like of “Zayd—where is his father?” (Zaydun ayna abūhu); for by its being placed after [the mubtadaʾ] the headship of that which has the head of the utterance is not annulled, since it stands at the head of its own sentence."},
    {"type": "matn",
     "ar": "(أو كان) الخبر بتقديمه[[٦]] (مصححا له[[٧]]) أي: للمبتدأ من حيث إنه مبتدأ، فتقديمه",
     "en": "“Or” the khabar, by its being placed first, “is what validates it,” that is, the mubtadaʾ insofar as it is a mubtadaʾ; so its placing first…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "من لم يقل بوجوب التقديم في مثل: «الزيدان قاما» لم يلتفت إلى الالتباس بالبدل أو الفاعل،",
     "en": "Whoever does not hold that placing first is obligatory in the like of “al-Zaydāni qāmā” paid no regard to confusion with the badal or the fāʿil,"},
    {"type": "pair",
     "ar": "بناء على أن السامع لا يحمل عليه لاستلزام عود الضمير قبل ذكر مرجعه، وخلاف الأصل.",
     "en": "on the basis that the hearer does not construe it so, because that would entail the pronoun's referring back before the mention of its antecedent, and [would be] contrary to the basic rule."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: وجوب التقديم في هذه الصورة مختلف فيه، فلو حمل مذهب الكتاب على عدم الوجوب لكان أخف.",
     "en": "It has been said: the obligatoriness of placing first in this case is disputed; so if the position of the book were taken to be non-obligatoriness, it would be lighter."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: نفسه؛ إذ لو تضمن متعلقه لا يجب إلا تقديم متعلقه، نحو: «غلام زيد راكب».",  # REVIEW: example printed as «غلام زيد راكب»; the point (a khabar whose dependent carries the interrogative) suggests a dropped «من» (غلام من), but transcribed as printed
     "en": "That is: [the khabar] itself; for if what is connected to it implicitly contained [such a meaning], only the placing first of what is connected to it would be obligatory, as in: “ghulāmu Zaydin rākibun.”"},
    {"type": "pair",
     "ar": "تفنن في العبارة حيث قال: «تضمن»، ولم يقل: «اشتمل».",
     "en": "It is a variation of expression, in that he said “implicitly contains” (taḍammana) and did not say “comprises” (ishtamala)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قيل: الموجب لتصدر الخبر منحصر في الاستفهام. وفيه نظر لمكان النفي نحو: «ما قائم زيد».",
     "en": "It has been said: what necessitates the khabar's standing at the head is restricted to the interrogative. This is open to question, given the case of negation, as in: “mā qāʾimun Zaydun” (Zayd is not standing)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "اعلم أن ما يقتضي صدر الكلام يكفيه أن يقع صدر جملة من الجمل بحيث لا يتقدم عليه شيء من ركني تلك الجملة،",
     "en": "Know that for what requires the head of the utterance it suffices that it occur at the head of some sentence, such that nothing of the two pillars of that sentence precedes it,"},
    {"type": "pair",
     "ar": "ولا ما صار من تمامها من الكلم المغيرة لمعناها كـ«أن» وسائر ما يحدث معنى من المعاني في الجملة التي تدخلها.",
     "en": "nor anything that has become part of its completion among the words that alter its meaning, such as “anna” and the rest of what produces some meaning in the sentence it enters."},
    {"type": "pair",
     "ar": "فلا يقال: «إن من تضربه أضربه».",
     "en": "So one does not say: “inna man taḍribhu aḍribhu” (Indeed, whomever you strike I will strike)."},
    {"type": "pair",
     "ar": "وأما جواز قولك: «الذي إن تضربه يضربك» فلأن الموصول لا يثير في صلته معنى.",
     "en": "As for the permissibility of your saying “alladhī in taḍribhu yaḍribka” (he who, if you strike him, will strike you), it is because the relative pronoun (mawṣūl) does not produce any meaning in its relative clause (ṣila)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "احترز عن كون الخبر بتأخيره مصححا لكونه مبتدأ نحو: «زيد قام»،",
     "en": "He excluded the case where the khabar, by its being placed after, validates [the other's] being a mubtadaʾ, as in “Zaydun qāma”;"},
    {"type": "pair",
     "ar": "فإن «زيدا» إنما يصح كونه مبتدأ لتأخر «قام»، حتى لو تقدم «قام» يجب كونه فاعلا.",
     "en": "for “Zayd” is valid as a mubtadaʾ only because “qāma” comes after it, so that if “qāma” came first, it would have to be the fāʿil."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "كما في «زيد قام»، فإنه لو أخر «زيد» لا يكون مبتدأ، بل يكون فاعل «قام».",
     "en": "As in “Zaydun qāma”: if “Zayd” were placed after, it would not be a mubtadaʾ but rather the fāʿil of “qāma.”"},
]
