# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 338 (printed ٣٣٧)."""

PAGE_NUMBER = 338
PRINTED_PAGE = "٣٣٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فلو حد المعطوف كذلك لدخل فيه بعض» at the foot of PDF p. 337.
    {"type": "matn",
     "ar": "الصفات مع أنه ليس بمعطوف.",
     "en": "…qualifiers would have entered it, although [such a qualifier] is not a conjoined noun."},
    {"type": "matn",
     "ar": "وقال بعضهم: فيه نظر؛ لأن الحروف المتوسطة بينها عاطفة لدلالتها فيها على ما تدل عليه في غيرها من الجمع والترتيب وغير ذلك،",
     "en": "Some of them said: this is open to question, since the particles intervening between them are conjunctive, because in them they indicate what they indicate elsewhere: combination, sequence and so on;"},
    {"type": "matn",
     "ar": "ففي جعلها غير عاطفة في الصفات عاطفة في غيرها ارتكاب أمر بعيد من غير ضرورة داعية إليه.",
     "en": "so to make them non-conjunctive among qualifiers and conjunctive elsewhere is to commit something far-fetched without any necessity calling for it."},
    {"type": "matn",
     "ar": "(وإذا عطف[[١]] على الضمير المرفوع) لا المنصوب والمجرور (المتصل) بارزا كان أو مستترا لا المنفصل (أكد[[٢]] بمنفصل[[٣]]) أولا ثم عطف عليه،",
     "en": "(When [a noun] is conjoined to the nominative pronoun), not the accusative or genitive one, (that is attached) (muttaṣil), whether visible or latent, not the detached one, (it is corroborated by a detached [pronoun]) first, and then [the noun] is conjoined to it."},
    {"type": "matn",
     "ar": "وذلك لأن المتصل المرفوع كالجزء مما اتصل به لفظا من حيث إنه متصل لا يجوز انفصاله، ومعنى من حيث إنه فاعل، والفاعل كالجزء من الفعل،",
     "en": "That is because the attached nominative [pronoun] is like a part of what it is attached to: in wording, inasmuch as it is attached and cannot be detached; and in meaning, inasmuch as it is the agent (fāʿil), and the agent is like a part of the verb."},
    {"type": "matn",
     "ar": "فلو عطف عليه بلا تأكيد كان كما لو عطف على بعض حروف الكلمة،",
     "en": "So were [a noun] conjoined to it without corroboration, it would be as if it were conjoined to some of the letters of the word."},
    {"type": "matn",
     "ar": "فأكد أولا بمنفصل؛ لأنه بذلك يظهر أن ذلك المتصل وإن كان كالجزء لكنه منفصل من حيث الحقيقة بدليل جواز إفراده مما اتصل به بتأكيده، فيحصل له نوع استقلال،",
     "en": "So it is first corroborated by a detached [pronoun], for thereby it becomes apparent that this attached [pronoun], though like a part, is in reality separate, as shown by the permissibility of setting it apart from what it is attached to by its corroboration; and so a kind of independence accrues to it."},
    {"type": "matn",
     "ar": "ولا يجوز أن يكون العطف على هذا التأكيد؛ لأن المعطوف في حكم المعطوف عليه، فكان يلزم أن يكون هذا المعطوف أيضا تأكيدا، وهو باطل،",
     "en": "The conjunction cannot be to this corroborative, since the conjoined noun has the status of the noun conjoined to, and it would then follow that this conjoined noun too is a corroborative, which is false."},
    {"type": "matn",
     "ar": "فإن كان الضمير منفصلا نحو: «ما ضرب إلا أنت وزيد» لم يكن كالجزء لفظا،",
     "en": "If the pronoun is detached, as in “mā ḍaraba illā anta wa-Zaydun” (none struck but you and Zayd), it is not like a part in wording;"},
    {"type": "matn",
     "ar": "وكذا إذا كان متصلا منصوبا نحو: «ضربتك وزيدا» لم يكن كالجزء معنى، فلا حاجة فيهما إلى التأكيد بمنفصل",
     "en": "likewise, when it is attached and accusative, as in “ḍarabtuka wa-Zaydan” (I struck you and Zayd), it is not like a part in meaning; so in neither case is there need for corroboration by a detached [pronoun]."},
    {"type": "matn",
     "ar": "(مثل: «ضربت أنا وزيد») و«زيدا ضرب هو وغلامه»",
     "en": "(As in “ḍarabtu anā wa-Zaydun” [I struck, I and Zayd]) and “Zaydan ḍaraba huwa wa-ghulāmuhu” (Zayd, he and his slave struck)."},
    {"type": "matn",
     "ar": "(إلا أن يقع فصل) بين الضمير المرفوع المتصل وبين ما عطف عليه (فيجوز تركه) أي: ترك التأكيد؛",
     "en": "(Unless a separation occurs) between the attached nominative pronoun and what is conjoined to it, (in which case its omission is permitted), that is, the omission of the corroboration,"},
    {"type": "matn",
     "ar": "لأنه قد طال الكلام[[٤]] بوجود المنفصل[[٥]]، فحسن الاختصار بترك التأكيد،",
     "en": "because the utterance has grown long through the presence of the detached [element], so brevity by omitting the corroboration is good;…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: إذا أريد العطف.",
     "en": "That is, when conjunction is intended."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يعاد الرافع كما يعاد الخافض؛ لأن التأكيد أخف من الإعادة.",
     "en": "The governor of the nominative is not repeated as the governor of the genitive is repeated, because corroboration is lighter than repetition."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فإن قلت: للتأكيد مقام وداع، فإذا لم يكن هناك داعي التأكيد كيف يعطف على الضمير المتصل؟",
     "en": "If you say: corroboration has its occasion and its motive; so when there is no motive for corroboration, how is [a noun] conjoined to the attached pronoun?"},
    {"type": "pair",
     "ar": "قلت: يعدل من عطف المفرد على المفرد إلى عطف الجملة على الجملة، فيقال: ضربت وضرب زيد،",
     "en": "I say: one turns from conjoining a single word to a single word to conjoining a sentence to a sentence, and says “ḍarabtu wa-ḍaraba Zaydun” (I struck, and Zayd struck)."},
    {"type": "pair",
     "ar": "ولما كان التأكيد بمنفصل احتاج إلى البيان؛ لأنه يحتمل تقديم التأكيد على العطف وتأخيره بينه بالمثال،",
     "en": "Since corroboration by a detached [pronoun] needed explanation, because the corroborative may come before or after the conjunction, he explained it by the example,"},
    {"type": "pair",
     "ar": "فقال: مثل ضربت أنا وزيد، واختاره على زيد ضرب هو وغلامه؛",
     "en": "saying: “as in ḍarabtu anā wa-Zaydun”; and he chose it over “Zaydun ḍaraba huwa wa-ghulāmuhu”,"},
    {"type": "pair",
     "ar": "لأنه الداعي على الحكم بالتأكيد في زيد ضرب هو وغلامه طردا للباب،",
     "en": "because [the first] is what prompts the ruling of corroboration in “Zaydun ḍaraba huwa wa-ghulāmuhu”, for the sake of the rule’s consistency;"},
    {"type": "pair",
     "ar": "وإلا فزيد ضرب هو وغلامه يحتمل أن يكون من قبيل انفصال الضمير للعطف لا من قبيل تأكيد المتصل بالمنفصل.",
     "en": "otherwise, “Zaydun ḍaraba huwa wa-ghulāmuhu” could be a case of the pronoun’s being detached for the sake of conjunction, not a case of corroborating the attached [pronoun] by the detached."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وطول الكلام قد يغني عما هو الواجب نحو قولك: حضر القاضي امرأة، والحافظو عورة بالنصب.",
     "en": "The length of the utterance sometimes dispenses with what is obligatory, as in your saying “ḥaḍara al-qāḍiya imraʾatun” (a woman came before the judge), and “al-ḥāfiẓū ʿawratan” (those who guard [their] nakedness) with the accusative."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هكذا في النسخ. والأظهر بوجود الفصل، أو يطول الكلام بالمنفصل.",
     "en": "Thus in the copies. The more evident reading is “through the presence of the separation”, or “the utterance grows long through the detached [pronoun]”."},
    {"type": "pair",
     "ar": "وقوله: فحسن الاختصار فيه أن طول الكلام حاصل لو أخر الفصل عن المعطوف مع أنه حين التأخر يتعين التأكيد، فإنه إذا قيل:",
     "en": "As for his words “so brevity is good”, [the objection] against them is that the length of the utterance would obtain if the separation were placed after the conjoined noun, although when it comes later corroboration is required; for if one says…"},
]
